<script>
    import IconButton from "../Buttons/iconButton.svelte";
    import { createEventDispatcher } from 'svelte';
    import DeleteTask from "../Detelor/DeleteTask.svelte";
    import ArchiveTask from "../Detelor/ArchiveTask.svelte";
    const dispatch = createEventDispatcher();
    const CloseIcon = '/icons/close_icon.svg';
    const DeleteIcon = '/icons/delete_icon.svg';
    const ArchiveIcon = '/icons/archive_icon.svg';

    const API_URL = 'http://127.0.0.1:5000';

    export let grouptype;
    export let task_id;
    export let task_status;
    export let watcher_id;
    export let author_id;
    export let executor_id;

    let changer = false;
    let deletor = false;
    let archivator = false;

    let task_delete = false;
    let task_archive = false;

    function CheckRights(){
        if(watcher_id == executor_id){
            changer = true;
        }
        if(watcher_id == author_id){
            deletor = true;
            if(grouptype == false){
                archivator = true;
            }
        }
    }

    function Cancel(){
        dispatch('cancel');
    }
    function SendNewStatus(){
        const data = {'status': task_status};
        dispatch('SendNewStatus', data);
    }
    async function StatusChanger(new_status){
        if(task_status != new_status){
            task_status = new_status;
            await ChangeStatus();
        }
    }

    async function ChangeStatus() {
        const response = await fetch(`${API_URL}/change_task_status`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task_id, task_status })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            return;
        }
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS');
            SendNewStatus();
            Cancel();
        } else {
            console.log('ERROR');
        }
    }
    function TaskDelete(){
        task_delete = true;
    }
    function CancelTaskDelete(){
        task_delete = false;
    }
    function TaskArchive(){
        task_archive = true;
    }
    function CancelTaskArchive(){
        task_archive = false;
    }
    function CancelTaskDeleteSuccess(){
        task_delete = false;
        Cancel();
    }
    function CancelTaskArchiveSuccess(){
        task_archive = false;
        Cancel();
    }
    CheckRights();
</script>


{#if task_delete}
    <DeleteTask task_id={task_id} user_id={author_id} on:cancel={CancelTaskDelete} on:cancelsuccess={CancelTaskDeleteSuccess}/>
{/if}
{#if task_archive}
    <ArchiveTask task_id={task_id} user_id={author_id} on:cancel={CancelTaskArchive} on:cancelsuccess={CancelTaskArchiveSuccess}/>
{/if}
<div class="status-block">
    <div class="closer">
        <div><IconButton icon={CloseIcon} onClick={Cancel}/></div>
    </div>
    {#if changer}
    <div class="changer">
        <div><button class="status {task_status == 1 ? 'active' : ''}" on:dblclick={() => StatusChanger(1)}><p>Не сделано</p></button></div>
        <div><button class="status {task_status == 2 ? 'active' : ''}" on:dblclick={() => StatusChanger(2)}><p>В процессе</p></button></div>
        <div><button class="status {task_status == 3 ? 'active' : ''}" on:dblclick={() => StatusChanger(3)}><p>Сделано</p></button></div>
        <div><button class="status {task_status == 4 ? 'active' : ''}" on:dblclick={() => StatusChanger(4)}><p>Отменено</p></button></div>
    </div>
    {/if}
    <div class="panel">
        {#if deletor}
            <div><IconButton icon={DeleteIcon} onClick={TaskDelete}/></div>
        {/if}
        {#if archivator}
            <div><IconButton icon={ArchiveIcon} onClick={TaskArchive}/></div>
        {/if}
    </div>
</div>

<style>
    .status-block{
        z-index: 10;
        width: 150px;
        height: fit-content;
        border: 1px solid #c5c9cf;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        background-color: white;
    }
    .status-block > div{
        width: 100%;
        height: fit-content;
    }
    .closer{
        display: flex;
        flex-direction: row;
        justify-content: end;
        align-items: center;
    }
    .changer{
        border-top: 1px solid #c5c9cf;
        display: flex;
        flex-direction: column;
    }

    .changer > div{
        border-bottom: 1px solid #c5c9cf;
        display: flex; justify-content: center;
        align-items: center; height: fit-content;
    }
    .changer > div button{
        height: 30px;
        width: 100%;
    }
    .status{
        background-color: inherit;
    }
    .status.active{
        background-color: #ccdbfd;
    }
    .status:hover{
        background-color: #edf2fa;
    }
    .panel{
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        align-items: center;
    }
    .panel > div{
        height: 40px;
        display: flex;
        justify-content: center; align-items: center;
    }


</style>