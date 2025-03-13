<script>
    import Calendar from "./Calendar.svelte";
    import Task from "../Tasks/Task.svelte";
    const API_URL = 'http://127.0.0.1:5000';

    export let user_id;

    let loading = false;
    let date = new Date();
    let dateString = date.toString();
    let task_ids = [];

    function PeopleDate(dateString) {
        const date = new Date(dateString);
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        return `${day}.${month}.${year}`;
    }

    function BaseDate(dateString){
        const date = new Date(dateString);
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        return `${year}-${month}-${day}`;
    }

    let selected_date = dateString;
    let converted_date = PeopleDate(dateString);
    let task_date = BaseDate(dateString);

    function GetDateFromCalendar(event) {
        selected_date = event.detail.selected_date;
        converted_date = PeopleDate(selected_date);
        task_date = BaseDate(selected_date);
        ShowDayTasks();
    }

    async function ShowDayTasks(){
        const response = await fetch(`${API_URL}/show_day_tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id, task_date })
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

    ShowDayTasks();
</script>
<style>
    .common-calendar{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
    .common-calendar > div{
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: center;
        margin: 10px;
    }
    .calendar-block{
        width: 380px;
        height: fit-content;
    }
    .day-items{
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: center;
        width: fit-content;
        height: fit-content;

    }
    .tasks{
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: center;
        width: 530px;
        border-radius: 8px;
        min-height: 60px;
        height: fit-content;
        max-height: 400px;
        background-color: #edf2fa;
        border: 1px solid #c5c9cf;
        overflow-x: visible;
        overflow-y: scroll;
    }
    .empty{
        width: fit-content;
        height: 60px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .tasks::-webkit-scrollbar{
        width: 6px;
        margin: 1px;
    }
    .tasks::-webkit-scrollbar-thumb{
        border-radius: 3px;
        background: #c5c9cf;
    }
</style>

<div class="common-calendar">
    <div class="calendar-block">
        <Calendar type='large' on:SendDateToPage={GetDateFromCalendar}/>
    </div>
    <div class="day-items">
        <div>
            <p>Мои задачи на {converted_date}</p>
        </div>
        
        <div class="tasks">
            {#if loading}
            {#if task_ids.length == 0}
            <div class="empty"><p>Пока тут пусто!</p></div>
            {:else}
            {#each task_ids as task_id}
            <Task task_id={task_id} watcher_id={user_id}/>
            {/each}
            {/if}
            {/if}
        </div>
    </div>
</div>
