<script>
    import CreateExecutor from "../Creator/CreateExecutor.svelte";
    import UserFriend from "./UserFriend.svelte";
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    export let watcher_id;
    export let subject_id;
    export let operation;

    const API_URL = 'http://127.0.0.1:5000';

    let header = '';
    let users_list;
    let loading = false;

    let executor_id = 0;
    let executor_name = '';

    function GetExecutor(event){
        executor_id = event.detail.executor_id;
        executor_name = event.detail.executor_name;
        SendThisExecutor();
    }

    function SendThisExecutor(){
        const data = {'executor_id': executor_id, 'executor_name': executor_name};
        dispatch('SendThisExecutor', data);
    }

    async function CheckOperation(){
        if(operation == 'friend_delete'){
            await ShowFriends();
            header = 'Мои друзья';
            loading = true;
        }
        else if( operation == 'executor_create' || operation == 'member_show'){
            await ShowMembers();
            loading = true;
        }
        else if (operation == 'member_delete'){
            await ShowMembers();
                header = 'Участники';
                users_list = users_list.filter(user => user !== watcher_id);
                console.log('УДАЛЕННЫЙ ЛИСТ = ', users_list )
                loading = true;
        }
        else if(operation == 'member_create'){
            header = 'Добавить участников';
            await ShowPossibleMembers();
            loading = true;
        }
        if( operation == 'executor_create'){
            header = 'Назначить исполнителя';
        }
        if(operation == 'member_show'){
            header = 'Участники';
        }
    }

    async function ShowFriends() {
        const response = await fetch(`${API_URL}/show_user_friends`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ watcher_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
        }
        const data = await response.json();
        if (data.status === 'success') {
            users_list = [];
            const user_ids = data.data;
            users_list = user_ids;
        } else {
            console.log('ERROR');
        }
    }

    async function ShowMembers() {
        const response = await fetch(`${API_URL}/show_list_members`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ watcher_id, subject_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
        }
        const data = await response.json();
        if (data.status === 'success') {
            users_list = [];
            const user_ids = data.data;
            users_list = user_ids;
        } else {
            console.log('ERROR');
        }
    }

    async function ShowPossibleMembers() {
        const response = await fetch(`${API_URL}/show_possible_list_members`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ watcher_id, subject_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            return;
        }
        const data = await response.json();
        if (data.status === 'success') {
            users_list = [];
            const user_ids = data.data;
            users_list = user_ids;
        } else {
            console.log('ERROR');
        }
    }

    CheckOperation();
</script>
<div class="main">
    <div><p class="p-task-desc">{header}</p></div>
    <div class="friends-block">
        {#if loading}
            {#if users_list.length === 0}
            <div class="message"><p class="p-light">Пока что тут никого нет.</p></div>
            {:else}
            {#each users_list as user_id}
                <div><UserFriend on:SendExecutor={GetExecutor} {watcher_id} {user_id} {subject_id} {operation}/></div>
            {/each}  
            {/if}   
        {/if}
    </div>
</div>


<style>
    .main{
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: center;
        border: 1px solid #c5c9cf;
        background-color: white;
        padding: 4px;
        border-radius: 8px;
    }
    .main > div{
        margin: 5px 0;
    }
    .friends-block{
        width: fit-content;
        display: flex;
        flex-direction: column;
        justify-content: start; align-items: center;
        min-width: 280px;
        min-height: 50px;
        height: fit-content;
        max-height: 200px;
        margin: 5px;
        border-radius: 8px;
        overflow-y: scroll;
        background-color: #edf2fa;
        border: 1px solid #c5c9cf;
    }
    .message {
        height: 50px;display: flex;
        justify-content: center; align-items: center;
    }
    .friends-block::-webkit-scrollbar{
        width: 6px;
        margin: 1px;
    }
    .friends-block::-webkit-scrollbar-thumb{
        border-radius: 3px;
        background: #c5c9cf;
    }
</style>