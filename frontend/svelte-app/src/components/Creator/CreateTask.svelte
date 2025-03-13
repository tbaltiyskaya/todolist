<script>
    import { createEventDispatcher } from 'svelte';
    import CreateExecutor from './CreateExecutor.svelte';
    import Friends from '../Users/Friends.svelte';
    import { linear } from 'svelte/easing';
    import DateTimeSelector from '../CommonCalendar/DateTimeSelector.svelte';
    import User from '../Users/User.svelte';
    import LargeButton from '../Buttons/LargeButton.svelte';
    const dispatch = createEventDispatcher();
    const API_URL = 'http://127.0.0.1:5000';
    
    const GroupIcon = '/icons/group_icon.svg';
    
    export let task_list;
    export let task_author;
    
    export let list_datetype;
    export let list_grouptype;


    let date = new Date();
    let time = null;
    let dateString = date.toString();
    let errorMessageName = '';
    let errorMessageDesc = '';
    let errorMessageTime = '';
    let correct_date = true;
    let canSent = false;

    let task_executor = task_author;
    let task_name = '';
    let task_desc = '';
    let task_date = null;
    let task_time = null;
    let task_priority = 2;

    function SetFirstDate(){
        if(list_datetype == true){
            const date = new Date();
            const formattedDate = date.toISOString().split('T')[0];
            task_date = formattedDate;
        }
        else{
            task_date = null;
        }
    }

    SetFirstDate();


    function CheckLength(){
        console.log('checklength');
    
        const MAX_NAME_LENGTH = 40;
        const MAX_DESC_LENGTH = 500;

        canSent = true;
        errorMessageName = '';
        errorMessageDesc = '';
        if (task_name.length > MAX_NAME_LENGTH) {
            errorMessageName = `Длина названия не должна превышать ${MAX_NAME_LENGTH} символов`;
            canSent = false;
        } else if (task_name.length === 0) {
            errorMessageName = 'Укажите название задачи';
            canSent = false;
        }

        if (task_desc.length > MAX_DESC_LENGTH) {
            errorMessageDesc = `Длина задачи не должна превышать ${MAX_DESC_LENGTH} символов`;
            canSent = false;
        }

        if (!correct_date) {
            canSent = false;
        }
        if (canSent) {
            errorMessageName = '';
            errorMessageDesc = '';
        }
        console.log('name ', task_name.length);
        console.log('canSent ', canSent);
    }

    function handleInputName(event) {
        task_name = event.target.innerText;
        CheckLength();
    }

    function handleInputDesc(event) {
        task_desc = event.target.innerText;
        CheckLength();
    }

    $: low = '#fff9c4';
    $: middle = '#fff9c4';
    $: high = 'transparent';
    
    function changePriority(level) {
        task_priority = level;
        if (task_priority == 3) {
            low = '#a5d6a7';
            middle = 'transparent';
            high = 'transparent';
        } 
        else if (task_priority == 2) {
            low = '#fff9c4';
            middle = '#fff9c4';
            high = 'transparent';
        }
        else if(task_priority == 1){
            low = '#ffcdd2';
            middle = '#ffcdd2';
            high = '#ffcdd2';
        } 
    }

    let executor_changer = false;

    function GetThisExecutor(event){
        task_executor = event.detail.executor_id;
        ChangeExecutor();
        console.log('THISexecutor_id: ', task_executor);
    }

    function CheckTime(date, time){
        let new_date;
        new_date = `${date} ${time}`;
        const timestamp = Date.parse(new_date);
        const dateObject = new Date(timestamp);
        let now = new Date();
        if(time == null){
            dateObject.setHours(0, 0, 0, 0);
            now.setHours(0, 0, 0, 0);
        }
        if(dateObject < now){
            errorMessageTime = 'Вы пытаетесь установить задачу на прошедшее время';
            correct_date = false;
            return false;
        }
        else{
            errorMessageTime = '';
            correct_date = true;
            return true;
        }

    }


    function GetNewDateTime(event){
        if (CheckTime(event.detail.task_date, event.detail.task_time) == false){
            CheckLength();
        }
        else{
            CheckLength();
            task_date = event.detail.task_date;
            task_time = event.detail.task_time;
        }
    }

    function ChangeExecutor(){
        executor_changer = !executor_changer;
    }
    
    function Cancel(){
        dispatch('cancel');
    }

    async function CreateTask() {
        const response = await fetch(`${API_URL}/create_task`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                task_list,
                task_author,
                task_executor,
                task_name,
                task_desc,
                task_date,
                task_time,
                task_priority
             })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            console.log('Нет соединения')
        }
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS');
            Cancel();
        } else {
            console.log('ERROR');
        }
    }

    CheckTime(task_date, task_time);
    CheckLength();

</script>

<div class="creator">
    <div class='block-header'><p>Создать задачу</p></div>
    <div class="data">
        <div class="header"><p>Заголовок</p></div>
        <div class="name" contenteditable="true"
            on:input={handleInputName} 
            placeholder="Введите имя">
        </div>
        <div class='warning'>
            <p>{errorMessageName}</p>
        </div>
        <div class="header"><p>Описание</p></div>
        <div class="desc" contenteditable="true"
            on:input={handleInputDesc} 
            placeholder="Введите описание">
        </div>
        <div class='warning'>
            <p>{errorMessageDesc}</p>
        </div>
    </div>
    {#if list_datetype}
    <div class="time">
        <DateTimeSelector task_date={dateString} task_time={time} on:SendOnEditor={GetNewDateTime} />
    </div>
    <div class='warning'>
        <p>{errorMessageTime}</p>
    </div>
    {/if}
    <div class="type">
        <div class="priority">
            <div><p class="p-task-desc">Приоритет</p></div>
            <div class='scale'>
              <div><button class='low' on:click={() => changePriority(3)}
                style={`background-color: ${low}`}><p>Низкий</p></button></div>
              <div><button class='middle' on:click={() => changePriority(2)}
                style={`background-color: ${middle}`}><p>Средний</p></button></div>
              <div><button class='high' on:click={() => changePriority(1)}
                style={`background-color: ${high}`}><p>Высокий</p></button></div>
            </div>
        </div>
        {#if list_grouptype}
        <div class="select-executor">
            <div class="selected-executor">
                <div><p class="p-task-desc">Исполнитель: </p></div>
                <div>
                    <div class="executor">
                        {#key task_executor}
                        <User user_id={task_executor}/>
                        {/key}
                    </div>
                    <div>
                    <LargeButton icon={GroupIcon} onClick={ChangeExecutor}/>
                    </div>
                </div>
                <div class="executor-changer {executor_changer ? 'active' : ''}">
                    {#if executor_changer}
                    <Friends on:SendThisExecutor={GetThisExecutor} watcher_id={task_author} subject_id={task_list} operation='executor_create'/>
                    {/if}  
                </div>
            </div>
        </div>
        {/if}
    </div>
    <div class="buttons">
        <button class="cancel" on:click={Cancel}><p>Отмена</p></button>
        <button class="save" disabled={!canSent} on:click|preventDefault={() => CreateTask()}><p>Создать</p></button>
    </div>
</div>


<style>
    .creator{
        position: absolute;
        top:10%; left: 30%;
        z-index: 10;
        width: 600px;height: fit-content;
        padding: 10px; border-radius: 8px;
        background-color: white;
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
        display: flex; flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
    .creator > div{
        width: 90%;
        margin: 4px;
        height: fit-content; 
    }
    .block-header{
        display: flex; justify-content: center; align-items: center;
        width: fit-content; height: 30px;
    }
    .block-header p{
        font-size: 16px;
        font-weight: 600;
    }
    .data{
        height: fit-content;
        display: flex; flex-direction: column;
        justify-content: start;
        align-items: center;
    }
    .data > div{
        width: 100%;
    }
    .name{
        height: fit-content;
        display: flex; align-items: center; flex-wrap: wrap;
        padding-left: 5px;
        font-size: 16px;
        border-bottom: 2px solid black;
    }
    .desc{
        height: fit-content;
        display: flex; align-items: center; flex-wrap: wrap;
        padding-left: 5px;
        font-size: 14px;
        border-bottom: 2px solid black;
    }
    .time{
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .type{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: start;
    }
    .type > div{
        height: 100%;
    }
    .priority{
        flex-direction: column; align-items: center; justify-content: space-between;
    }
    .scale{
        display: flex; flex-direction: row;
        width: fit-content;
        border: 1px solid #c5c9cf;
        border-radius: 4px;
        overflow: hidden;
        margin: 4px;
    }
    .scale > div{
        width: 60px;
        height: 20px;
        display: flex;
    }
    .scale > div button{
        width: 60px;
        height: 20px;
        display: flex;
        justify-content: center; align-items: center;
    }
    .scale div p{
        font-size: 12px;
    }
    .select-executor{
        height: fit-content;
        display: flex; flex-direction: column;
        justify-content: start;
        align-items: start;
        position: relative;
    }
    .selected-executor{
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: start;
        margin-bottom: 5px;
    }
    .selected-executor > div{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    .executor-changer{
        display: none;
        width: 0; height: 0;
    }
    .executor-changer.active{
        display: flex;
        position: absolute;
        top: 80px;
        right: 0;
        width: fit-content;
        height: fit-content;
    }
    .executor{
        border: 1px solid #c5c9cf;
        border-radius: 8px;
    }
    .buttons{
        height: fit-content;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    .buttons button{
        background-color: #abc4ff;
        border-radius: 8px;
        width: 90px;
        height: 30px;
        transition: all 0.2s ease;
    }
    .buttons button:disabled{
        cursor: not-allowed;
        background-color: #edf2fa;
    }
    .buttons button:hover{
        background-color: #c1d3fe;
    }
    .buttons button:active{
        transform: scale(97%);
    }
    .buttons button p{
        font-size: 12px;
        font-weight: 400;
    }
    .warning{
        height: 30px;
        display: flex; justify-content: center; align-items: center;
    }
    .warning p{
        text-align: center;
        font-size: 12px;
        font-weight: 300;
        color: red;
    }
</style>