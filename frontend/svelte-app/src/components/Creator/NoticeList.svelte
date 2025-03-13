<script>
    import { createEventDispatcher } from 'svelte';
    import User from '../Users/User.svelte';
    const dispatch = createEventDispatcher();
    const API_URL = 'http://127.0.0.1:5000';
    
    export let notice_id;

    let loading = false;
    let my_id;
    let user_id;
    let list_id;
    let status;
    let list_name;


    function Cancel(){
        const data = {'notice_id': notice_id};
        dispatch('cancel', data);
    }

    
    async function GetNotice() {
        const response = await fetch(`${API_URL}/get_list_notice`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ notice_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            console.log('Нет соединения')
        }
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            const {sender: fetchedsender, getter: fetchedgetter, list: fetchedlist, list_name: fetchedlistname} = data.data;
            user_id = fetchedsender;
            my_id = fetchedgetter;
            list_id = fetchedlist;
            list_name = fetchedlistname;
            loading = true;
        } else {
            console.log('ERROR');
        }
    }

    async function RespAdd() {
        const response = await fetch(`${API_URL}/resp_add_member`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ notice_id, status })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            console.log('Нет соединения')
        }
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            Cancel();
        } else {
            console.log('ERROR');
        }
    }

    async function SetStatus(notice_status){
        status = notice_status;
        await RespAdd();
    }

    
    GetNotice();
</script>


<div class="deletor">
    <div class='block-header'><p>Приглашение в лист "{list_name}":</p></div>
    <div class="data">
        {#if loading}
        <div><User user_id={user_id}/></div>
        {/if}
    </div>
    <div class="buttons">
        <button class="cancel" on:click={SetStatus(false)}><p>Отклонить</p></button>
        <button class="save" on:click|preventDefault={() => {SetStatus(true)}}><p>Принять</p></button>
    </div>
</div>


<style>
    .deletor{
        margin: 4px;
        z-index: 20;
        width: 300px; height: 150px;
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
        width: fit-content; height: fit-content;
    }
    .block-header p{
        font-size: 16px;
        font-weight: 600;
    }
    .data{
        height: 200px;
        display: flex; flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .data > div{
        width: fit-content;
        padding: 4px;
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
</style>