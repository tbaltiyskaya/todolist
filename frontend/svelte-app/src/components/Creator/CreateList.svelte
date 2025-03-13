<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    const API_URL = 'http://127.0.0.1:5000';
    
    export let user_id;
    let errorMessage = '';
    let canSent = false;

    let tempName = '';
    let groupType = false;
    let dateType = false;

    function CheckLength(){
        if (tempName.length > 40){
            errorMessage = 'Длина названия не должна превышать 40 символов';
            canSent = false;
        }
        else if(tempName.length == 0){
            errorMessage = 'Укажите название листа';
            canSent = false;
        }
        else{
            errorMessage = '';
            canSent = true;
        }
    }
    function ChangeGroupType(){
        groupType = !groupType;
    }

    function ChangeDateType(){
        dateType = !dateType;
    }

    function handleInput(event) {
        tempName = event.target.innerText;;
        CheckLength();
    }
    
    function Cancel(){
        dispatch('cancel');
    }

    async function CreateList() {
        const response = await fetch(`${API_URL}/create_list`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id, tempName, groupType, dateType })
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
            errorMessage = 'SUCCESS';
            Cancel();
        } else {
            console.log('ERROR');
        }
    }


</script>

<div class="creator">
    <div class='block-header'><p>Создать лист</p></div>
    <div class="data">
        <div class="header"><p>Название листа</p></div>
        <div class="name" contenteditable="true"
            on:input={handleInput} 
            placeholder="Введите имя">
        </div>
        <div class='warning'>
            <p>{errorMessage}</p>
        </div>
        <div class="type">
            <div>
                <div class="header"><p>Датированый</p></div>
                <button class="toggle" on:click={() => ChangeDateType()}>
                    <div class="oval {dateType ? 'active' : ''}">
                        <div class="round"></div>
                    </div>
                </button>
            </div>
            <div>
                <div class="header"><p>Групповой</p></div>
                <button class="toggle"  on:click={() => ChangeGroupType()}>
                    <div class="oval {groupType ? 'active' : ''}">
                        <div class="round"></div>
                    </div>
                </button>
            </div>
        </div>

    </div>
    <div class="buttons">
        <button class="cancel" on:click={Cancel}><p>Отмена</p></button>
        <button class="save" disabled={!canSent} on:click|preventDefault={() => CreateList()}><p>Создать</p></button>
    </div>
</div>


<style>
    .creator{
        position: absolute;
        top:10%; left: 30%;
        z-index: 10;
        width: 400px;height: 300px;
        padding: 10px; border-radius: 8px;
        background-color: white;
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
        display: flex; flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
    .creator > div{
        width: 90%;
    }
    .block-header{
        display: flex; justify-content: center; align-items: center;
        width: fit-content; height: 30px;
    }
    .block-header p{
        font-size: 16px;
        font-weight: 600;
    }
    .header{
        display: flex; justify-content: center; align-items: center;
        width: fit-content; height: 30px;
    }
    .header p{
        font-size: 14px;
        font-weight: 500;
    }
    .data{
        height: 200px;
        display: flex; flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
    .data > div{
        width: 100%;
    }
    .name{
        min-height: 25px;
        display: flex; align-items: center; flex-wrap: wrap;
        padding-left: 5px;
        font-size: 16px;
        border-bottom: 2px solid black;
    }
    .type{
        display: flex; flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    .type > div{
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
    .toggle{
        width: 70px;
        height: 40px;
        margin: 10px;
    }
    .oval{
        width: 60px; height: 30px;
        border-radius: 26px;
        background-color: #edf2fa;
        display: flex; flex-direction: row;
        justify-content: start; align-items: center;
        transition: all 0.3s ease;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
    }
    .round{
        margin: 5px;
        background-color: white;
        width: 26px; height: 26px;
        border-radius: 50%; box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
    }
    .oval.active{
        background-color: #c1d3fe;
        justify-content: end;
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