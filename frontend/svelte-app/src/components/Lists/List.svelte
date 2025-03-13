<!-- Страница для отображения листа -->
<script>
    import IconButton from "../Buttons/iconButton.svelte";
    import LargeButton from "../Buttons/LargeButton.svelte";
    import Calendar from "../CommonCalendar/Calendar.svelte";
    import CreateTask from "../Creator/CreateTask.svelte";
    import AddUsers from "../Editor/AddUsers.svelte";
    import Task from "../Tasks/Task.svelte";
    import Friends from "../Users/Friends.svelte";
    const API_URL = 'http://127.0.0.1:5000';
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    export let user_id;
    export let list_id;
    export let list_name;
    export let list_author;
    export let list_datetype;
    export let list_grouptype;

    let wish_progress;
    let progress;
    let user_progress;

    $: progress_bar = ((progress/wish_progress) * 200) | 0;
    $: user_progress_bar = ((user_progress/wish_progress) * 200)| 0;

    const BackIcon = '/icons/back_icon.svg';
    const AddIcon = '/icons/plus_icon.svg';
    const GroupIcon = '/icons/group_icon.svg';
    const CloseIcon = '/icons/close_icon.svg';

    function Cancel(){
        dispatch('cancel');
    }

    function BaseDate(date){
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        return `${year}-${month}-${day}`;
    }
    let loading = false;
    const today = new Date();
    let task_ids = [];
    let task_date = BaseDate(today);
    let navbutton = 'own';
    let show_members = false;
    let member_add = false;
    let create_task = false;

    function ShowGroupMembers(){
        show_members = !show_members;
    }
    function TaskCreate(){
        create_task = true;
    }
    
    function GetDateFromCalendar(event) {
        let date = event.detail.selected_date;
        task_date = BaseDate(date);
        ChangeNav(navbutton);
        GetProgress();
    }

    async function GetProgress(){
        console.log('DATE = ', task_date)
        const response = await fetch(`${API_URL}/get_progress`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({  list_id, user_id, task_date })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            return;
        }
        const data = await response.json();
        if (data.status === 'success') {
            const {
                wish_progress: fetchedwish_progress,
                progress: fetchedprogress,
                user_progress: fetcheduser_progress,
                } = data.data;
                wish_progress = fetchedwish_progress;
                progress = fetchedprogress;
                user_progress = fetchedprogress;
                progress_bar = ((progress/wish_progress) * 200) | 0;
                user_progress_bar = ((user_progress/wish_progress) * 200)| 0;
                console.log("PROGRESS", wish_progress, progress_bar, user_progress_bar);
        } else {
            console.log('ERROR');
        }
    }
    
    async function ShowOwnTasks(){
        console.log('DATE = ', task_date)
        const response = await fetch(`${API_URL}/show_own_list_tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id, list_id, list_datetype, task_date })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            return;
        }
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS');
            task_ids = [];
            const tasks = data.data;
            task_ids = tasks;
            console.log("tasks = ",task_ids);
            loading = true;
        } else {
            console.log('ERROR');
        }
    }

    async function ShowAuthoredTasks(){
        const response = await fetch(`${API_URL}/show_authored_list_tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id, list_id, list_datetype, task_date })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            return;
        }
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS');
            task_ids = [];
            const tasks = data.data;
            task_ids = tasks;
            console.log("tasks = ",task_ids);
            loading = true;
        } else {
            console.log('ERROR');
        }
    }

    async function ShowAllTasks(){
        const response = await fetch(`${API_URL}/show_all_list_tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id, list_id, list_datetype, task_date })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            return;
        }
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS');
            task_ids = [];
            const tasks = data.data;
            task_ids = tasks;
            console.log("tasks = ",task_ids);
            loading = true;
        } else {
            console.log('ERROR');
        }
    }
    
    async function ChangeNav(nav){
        loading = false;
        navbutton = nav;
        if(nav === 'own'){
            await ShowOwnTasks();
        }
        else if(nav === 'author'){
            await ShowAuthoredTasks();
        }
        else if(nav === 'all'){
            await ShowAllTasks();
        }
    }

    function CancelTaskCreate(){
        create_task = false;
        ChangeNav(navbutton);
    }

    function GetTaskUpdates(){
        ChangeNav(navbutton);
    }

    function MemberAdd(){
        member_add = true;
    }
    function CancelMemberAdd(){
        member_add = false;
    }

    ShowOwnTasks();
    GetProgress();
</script>
    
<div class='list'>
    {#if member_add}
        <AddUsers list_id={list_id} author_id={list_author} on:cancel={CancelMemberAdd}/>
    {/if}
    {#if create_task}
        <CreateTask on:cancel={CancelTaskCreate} task_list={list_id} task_author={user_id} 
        list_datetype={list_datetype} list_grouptype={list_grouptype}/>
    {/if}
    <div class='head'>
        <div><LargeButton icon={BackIcon} onClick={Cancel}/></div>
        <div class="list-name"><p class="p-header">{list_name}</p></div>
        <div class="group">
            {#if list_grouptype}
            {#if !show_members}
            <LargeButton onClick={ShowGroupMembers} icon={GroupIcon}/>
            {:else}
            <LargeButton onClick={ShowGroupMembers} icon={CloseIcon}/>
            {/if}
            {/if}
        </div>
        <div class='members {show_members ? 'active' : ''}'>
            {#if show_members}
                {#if user_id == list_author}
                    <Friends watcher_id={user_id} subject_id={list_id} operation='member_delete'/>
                    <div class="add-member">
                        <p class="p-light">Добавить участников</p>
                        <IconButton icon={AddIcon} onClick={MemberAdd}/>
                    </div>
                {:else}
                    <Friends watcher_id={user_id} subject_id={list_id} operation='member_show'/>
                {/if}
            {/if}
        </div>
    </div>
    <div class="main">
        <div class="progress">
            {#if list_grouptype}
            <div><p>Общий прогресс</p></div>
            <div class="wish-progress">
                <div class="all-progress" style="width: {progress_bar}px;"></div>
            </div>
            {/if}
            <div><p>Ваш прогресс</p></div>
            <div class="wish-progress">
                <div class="user-progress" style="width: {user_progress_bar}px;"></div>
            </div>
        </div>
        <div class="task-container">
            {#if list_datetype}
            <div class="calendar">
                <Calendar type='week' on:SendDateToPage={GetDateFromCalendar}/>
            </div>
            {/if}
            <div class="nav">
                {#if list_grouptype}
                <button on:click={() => ChangeNav('own')}><p class="p-light {navbutton == 'own' ? 'active' : ''}">Личные задачи</p></button>
                <button on:click={() => ChangeNav('author')}><p class="p-light {navbutton == 'author' ? 'active' : ''}">Выданные мной</p></button>
                {#if user_id == list_author}
                <button on:click={() => ChangeNav('all')}><p class="p-light {navbutton == 'all' ? 'active' : ''}">Все задачи</p></button>
                {/if}
                {:else}
                <div><p class="p-light">Мои задачи</p></div>
                {/if}
                <IconButton icon={AddIcon} onClick={TaskCreate}/>
            </div>
            {#key create_task}
            <div class="tasks">
                {#if loading}
                {#each task_ids as task_id}
                <Task 
                task_id={task_id}
                watcher_id={user_id} on:SendUpdates={GetTaskUpdates}
                />
                {/each}
                {/if}
            </div>
            {/key}
        </div>
    </div>
</div>


<style>
    .list{
        width: 100%;
        height: 100%;
        display: flex; flex-direction: column;
        justify-content: start; align-items: center;
    }
    .list-name{
        min-width: 300px;
    }
    .group{
        width: 160px;
    }
    .list > div{
        width: 100%;
    }
    .head{
        height: 40px;
        border-bottom: 1px solid #c5c9cf;
        display: flex; flex-direction: row;
        justify-content: space-between;
        position: relative;
    }
    .head > div{
        margin: 10px 40px 10px 10px;
        display: flex; justify-content: center; align-items: center;
    }
    .members{
        display: none;
        position: absolute;
        margin: 0;
    }
    .members.active{
        margin: 0;
        z-index: 11;
        position: absolute; top: 100%; right: 0;
        border-radius: 8px;
        background-color: white; border: 1px solid #c5c9cf;
        width: fit-content; height: fit-content;
        display: flex; flex-direction: column;
        justify-content: start; align-items: center;
    }
    .add-member{
        display: flex; flex-direction: row;
        justify-content: space-around; align-items: center;
        width: 250px;height: fit-content;
    }
    .main{ 
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: start;
        height: 100%;
    }
    .main > div{
        margin: 0;
    }
    .progress{
        width: 300px;
        height: 100%;
        border-left: 1px solid #c5c9cf;
        display: flex; flex-direction: column;
        justify-content: start;
        align-items: center;
        margin-top: 50px;
    }
    .progress > div{
        margin: 4px;
    }
    .wish-progress{
        border: 1px solid #c5c9cf;
        height: 24px;
        width: 200px;
        background-color: #edf2fa;
        border-radius: 12px;
        display: flex;
        flex-direction: row;
        justify-content: start;
        align-items: center;
    }
    .all-progress{
        margin: 4px;
        height: 16px;
        border-radius: 12px;
        background-color: #ccdbfd;
        box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
    }
    .user-progress{
        margin: 4px;
        height: 16px;
        border-radius: 12px;
        box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
        background-color: #abc4ff;
    }
    .task-container{
        display: flex; flex-direction: column;
        justify-content: start; align-items: center;
        width: 500px; padding: 6px;
        height: 100%;
        background-color: #edf2fa;
        border: 1px solid #c5c9cf;
    }
    .task-container > div{
        width: 100%;
    }
    .calendar{
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .nav{
        background-color: white;
        border: 1px solid #c5c9cf;
        margin: 0 10px;
        height: fit-content;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
    }
    .tasks{
        width: 100%; padding: 6px;
        min-height: 40px;
        display: flex; flex-direction: column;
        justify-content: start; align-items: center;
    }
</style>
