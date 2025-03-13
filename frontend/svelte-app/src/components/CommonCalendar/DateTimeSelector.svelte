<script>
    import IconButton from "../Buttons/iconButton.svelte";
    import Calendar from "./Calendar.svelte";
    import TimeSelector from "./TimeSelector.svelte";
    const CalendarIcon = '/icons/calendar_icon.svg';
    const TimeIcon = '/icons/time_icon.svg';
    const CloseIcon = '/icons/close_icon.svg';
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

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


    export let task_date;
    export let task_time;

    console.log('task_date = ', task_date);
    console.log('task_time = ', task_time);

    let converted_date = '';
    let converted_time = '';

    $: {
         {
            let dateObject = new Date(task_date);
            converted_date = PeopleDate(dateObject);
            if(task_time == null){
                converted_time = 'Нет';
            }
            else{converted_time = task_time};
        }
    }

    let show_calendar = false;
    let show_timer = false;
    function ShowCalendar(){
        show_calendar = !show_calendar;
    }
    function ShowTimer(){
        show_timer = !show_timer;
    }
    function CancelTimer(){
        show_timer = false;
        converted_time = 'Нет';
        task_time = null;
        SendOnEditor();
    }
    function GetDateFromCalendar(event) {
        task_date = event.detail.selected_date;
        converted_date = PeopleDate(task_date);
        ShowCalendar();
        SendOnEditor();
    }
    function GetTimeFromSelector(event) {
        task_time = event.detail.selected_time;
        converted_time = task_time;
        ShowTimer();
        SendOnEditor();
    }

    function SendOnEditor(){
        const data = {'task_date': BaseDate(task_date), 'task_time': task_time};
        dispatch('SendOnEditor', data);
        console.log(data);
    }

    

    
</script>

<div class="datechecker">
    <div class="date">
        <div class="date-field">
            <div><p class="p-task-desc">Дата: {converted_date}</p></div>
            <div><IconButton icon={CalendarIcon} onClick={ShowCalendar}/></div>
        </div>
        <div class="calendar {show_calendar ? 'active' : ''}">
            {#if show_calendar}
            <Calendar type='mini' on:SendDateToPage={GetDateFromCalendar}/>
            {/if}
        </div>
    </div>
    <div class="time">
        <div class="time-field">
            <div><p class="p-task-desc">Время: {converted_time}</p></div>
            <div class="time-panel">
                <IconButton icon={TimeIcon} onClick={ShowTimer}/>
                <IconButton icon={CloseIcon} onClick={CancelTimer}/>
            </div>
        </div>
        <div class="timer {show_timer ? 'active' : ''}">
            {#if show_timer}
            <TimeSelector on:SendTimeToPage={GetTimeFromSelector}/>
            {/if}
        </div>
    </div>
</div>

<style>
    .datechecker{
        width: 400px;
        height: 30px;
        display: flex; flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    .date{
        width: 200px;
        height: 100%;
        border-right: 1px solid #c5c9cf;
        position: relative;
    }
    .date-field{
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    .date-field > div{
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .calendar{
        display: none;
    }
    .calendar.active{
        display: flex;
        position: absolute;
        z-index: 12;
        top: 30px;
        right: 0;
    }
    .time{
        width: 200px;
        height: 100%;
        position: relative;
    }
    .time-field{
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    .time-panel{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    .timer{
        display: none;
    }
    .timer.active{
        display: flex;
        position: absolute;
        z-index: 12;
        top: 30px;
        right: 0;
    }
</style>