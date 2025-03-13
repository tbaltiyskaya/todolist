<script>
    import CreateList from "../Creator/CreateList.svelte";
    import Task from "../Tasks/Task.svelte";
    export let user_id;
    let archived_tasks = [];

    let loading = false;

    const API_URL = 'http://127.0.0.1:5000';

    async function ShowArchivedTasks() {
        const response = await fetch(`${API_URL}/show_archived_tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id})
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            console.log('Нет соединения')
        }
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            const taskIds = data.data;
            archived_tasks = [];
            archived_tasks = taskIds;
            loading = true;
        } 
        else {
            console.log('ERROR');
        }
    }

    function GetTaskUpdates(){
        ShowArchivedTasks();
    }
    ShowArchivedTasks();

</script>
    

<div class="archive">
    <div><p>Архив задач</p></div>
    <div class="archive-tasks">
        {#if loading}
        {#if archived_tasks.length == 0}
        <div class="empty"><p>Нет задач в архиве!</p></div>
        {:else}
        {#each archived_tasks as task_id}
        <Task task_id={task_id} watcher_id={user_id} on:SendUpdates={GetTaskUpdates}/>
        {/each}
        {/if}
        {/if}
    </div>
</div>

<style>
    .archive{
        width: 100%;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: center;
    }
    .empty{
        width: fit-content;
        height: 60px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .archive-tasks{
        height: fit-content;
        max-height: 500px;
        width: 520px;
        background-color: #edf2fa;
        border: 1px solid #c5c9cf;
    }
</style>