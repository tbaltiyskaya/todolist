<script>
    import IconButton from "../Buttons/iconButton.svelte";
    import { createEventDispatcher } from 'svelte';
    import ListName from "../Lists/ListName.svelte";
    const dispatch = createEventDispatcher();
    const CloseIcon = '/icons/close_icon.svg';

    const API_URL = 'http://127.0.0.1:5000';

    export let task_id;
    export let author_id;

    let loading = false;
    let author_lists = [];
    let task_list;
    

    function Cancel(){
        dispatch('cancel');
    }

    async function ShowOwnLists() {
        const user_id = author_id;
        const response = await fetch(`${API_URL}/show_own_lists`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            console.log('Нет соединения')
        }
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS LISTS OWN');
            const listIds = data.data;
            author_lists = [];
            author_lists = listIds;
            loading = true;
        } 
        else {
            console.log('ERROR');
        }
    }


    async function UnzipTask() {
        const response = await fetch(`${API_URL}/unzip_task`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task_id, task_list})
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            return;
        }
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS');
            Cancel();
        } else {
            console.log('ERROR');
        }
    }

    function GetSelectedId(event){
        task_list = event.detail.list_id;
        UnzipTask();
    }
    
    ShowOwnLists();

</script>


<div class="status-block">
    <div class="closer">
        <div><p class="p-task-name">Выбрать лист</p></div>
        <div><IconButton icon={CloseIcon} onClick={Cancel}/></div>
    </div>
    <div class="changer">
        {#each author_lists as list_id}
            <div>
                <ListName list_id={list_id} on:SendListId={GetSelectedId}/>
            </div>
        {/each}
    </div>
</div>

<style>
    .status-block{
        z-index: 10;
        width: 200px;
        height: fit-content;
        border: 1px solid #c5c9cf;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        background-color: white;
    }
    .status-block > div{
        width: 100%;
    }
    .closer{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        height: fit-content;
    }
    .changer{
        border-top: 1px solid #c5c9cf;
        display: flex;
        flex-direction: column;
        height: 140px;
        overflow-y: scroll;
        width: fit-content;

    }
    .changer::-webkit-scrollbar{
        width: 6px;
        margin: 1px;
    }
    .changer::-webkit-scrollbar-thumb{
        border-radius: 3px;
        background: #c5c9cf;
    }
    .changer > div{
        border-bottom: 1px solid #c5c9cf;
        display: flex; justify-content: center;
        align-items: center; height: fit-content;
    }


</style>