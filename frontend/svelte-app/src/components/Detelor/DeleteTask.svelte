<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    const API_URL = 'http://127.0.0.1:5000';
    
    export let task_id;
    export let user_id;


    function Cancel(){
        dispatch('cancel');
    }
    function CancelSuccess(){
        dispatch('cancelsuccess');
    }


    async function DeleteTask() {
        const response = await fetch(`${API_URL}/delete_task`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task_id, user_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            console.log('Нет соединения')
        }
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            CancelSuccess();
        } else {
            console.log('ERROR');
        }
    }
</script>


<div class="deletor">
    <div class='block-header'><p>Удалить задачу</p></div>
    <div class="data">
        <div class="header"><p>Вы действительно хотите удалить задачу?</p></div>
    </div>
    <div class="buttons">
        <button class="cancel" on:click={Cancel}><p>Отмена</p></button>
        <button class="save" on:click|preventDefault={() => DeleteTask()}><p>Удалить</p></button>
    </div>
</div>


<style>
    .deletor{
        position: absolute;
        top:50%; left: 50%;
        z-index: 12;
        width: 400px; height: 120px;
        padding: 10px; border-radius: 8px;
        background-color: white;
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
        display: flex; flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
    .deletor > div{
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
    .data{
        height: 200px;
        display: flex; flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
    .data > div{
        width: 100%;
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
</style>