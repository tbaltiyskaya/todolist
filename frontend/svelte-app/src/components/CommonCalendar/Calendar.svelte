<script>
    import { createEventDispatcher } from 'svelte';
    import IconButton from "../Buttons/iconButton.svelte";
    import LargeButton from "../Buttons/LargeButton.svelte";
    import DateComponent from "./Date.svelte";
    const dispatch = createEventDispatcher();
    const ToRightIcon = "icons/toright_icon.svg";
    const ToLeftIcon = "icons/toleft_icon.svg"
    const monthNames = [
        "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
    ];
    const weekDays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"];

    let blockNext = false;
    let blockLast = false;

    export let type;
    let SelectedDate = new Date();
    let emptyDays = 0;
    let currentMonth = SelectedDate.getMonth();
    let currentYear = SelectedDate.getFullYear();
    let MonthList = [];
    let currentWeekStart;
    let WeekList = [];
    $: ManageString = monthNames[currentMonth] + " " + currentYear;

    function generateMonth(){
        MonthList = [];
        var thisDate = new Date(currentYear, currentMonth, 1);
        emptyDays = thisDate.getDay() === 0 ? 6 : thisDate.getDay() - 1;
        while(thisDate.getMonth() == currentMonth){
            MonthList.push(new Date(thisDate));
            thisDate.setDate(thisDate.getDate() + 1);
        }
    }

    function InitCurrentWeek(){
        const today = new Date();
        const currentDay = today.getDay();
        const mondayOffset = (currentDay === 0) ? -6 : 1 - currentDay;
        currentWeekStart = new Date(today);
        currentWeekStart.setDate(today.getDate() + mondayOffset);
        GenerateWeek();
    }

    function GenerateWeek(){
        WeekList = [];
        for (let i = 0; i < 7; i++) {
            let date = new Date(currentWeekStart);
            date.setDate(currentWeekStart.getDate() + i);
            WeekList.push(date);
        }
        console.log(WeekList);
    }

    function GetDate(event) {
        SelectedDate = event.detail.selected_date;
        SendDateToPage();
    }
    function SendDateToPage(){
        const data = {'selected_date': SelectedDate};
        dispatch('SendDateToPage', data);
    }

    function ShowLastMonth(){
        if(currentMonth > 0){
            currentMonth = currentMonth-1;
        }
        else{
            currentMonth = 11;
            currentYear = currentYear-1;
        }
        generateMonth();
        CheckDifference();
    }
    function ShowNextMonth(){
        if(currentMonth < 11){
            currentMonth+=1;
        }
        else{
            currentMonth = 0;
            currentYear += 1;
        }
        generateMonth();
        CheckDifference();
    }
    function ShowLastWeek(){
        currentWeekStart.setDate(currentWeekStart.getDate() - 7);
        GenerateWeek();
    }
    function ShowNextWeek(){
        currentWeekStart.setDate(currentWeekStart.getDate() + 7);
        GenerateWeek();
    }
    

    function CheckDifference(){
        var thisYear = new Date().getFullYear();
        if (currentYear - thisYear > 2){
            blockNext = true;
        }
        else if(thisYear - currentYear > 2){
            blockLast = true;
        }
        else if (Math.abs(currentYear - thisYear) <=2){
            blockLast = false;
            blockNext = false;
        }
    }

    function CheckType(){
        if(type == 'large' || type == 'mini'){
            generateMonth();
        }
        else if(type == 'week'){
            InitCurrentWeek();
        }
    }
    CheckType();
</script>

<style>
    .calendar{
        width: 340px;
        height: 340px;
        padding: 10px;
        box-shadow: rgba(0, 0, 0, 0.18) 0px 2px 4px;
        background-color: #edf2fa;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        justify-content:start;
        align-items: center;
    }
    .calendar.mini{
        width: 180px;
        height: 200px;
        padding: 5px;
        box-shadow: rgba(0, 0, 0, 0.18) 0px 2px 4px;
        background-color: #edf2fa;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        justify-content:start;
        align-items: center;
    }
    .calendar.week{
        width: 500px;
        height: 120px;
        box-shadow: rgba(0, 0, 0, 0.18) 0px 2px 4px;
        background-color: #edf2fa;
        display: flex;
        flex-direction: column;
        justify-content:start;
        align-items: center;
        box-shadow: none;
        border-radius: 0px;
    }
    .manage{
        width: fit-content;
        height: fit-content;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    .managestring{
        width: 120px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .managestring.mini{
        width: 110px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .week-days{
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }
    .week-day{
        display: flex;
        justify-content: center;
        align-items: center;
        width: fit-content;
        height: fit-content;
        margin: 8px 8px;
        width: 26px;
        height: 26px;
    }
    .week-day.mini{
        display: flex;
        justify-content: center;
        align-items: center;
        width: fit-content;
        height: fit-content;
        margin: 4px 4px;
        width: 16px;
        height: 16px;
    }
    .dates{
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        grid-template-rows: repeat(6, 1fr);
    }
    .dates.week{
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        grid-template-rows: repeat(1, 1fr);
    }
    .day{
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 4px;
        margin: 8px 8px;
        width: 26px;
        height: 26px;
    }
    .day.mini{
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 4px;
        margin: 4px 4px;
        width: 16px;
        height: 16px;
    }
    .empty {
        grid-column: span 1;
    }
</style>

<div class="calendar {type === 'mini' ? 'mini' : ''} {type === 'week' ? 'week' : ''}">
    <div class="manage">
        {#if type == 'large'}
        <LargeButton icon={ToLeftIcon} disabled={blockLast} onClick={ShowLastMonth}/>
        <div class="managestring {type === 'mini' ? 'mini' : ''}"><p class="p-bold">{ManageString}</p></div>
        <LargeButton icon={ToRightIcon} disabled={blockLast} onClick={ShowNextMonth}/>
        {:else if type == 'mini'}
        <IconButton icon={ToLeftIcon} disabled={blockLast} onClick={ShowLastMonth}/>
        <div class="managestring {type === 'mini' ? 'mini' : ''}"><p class="p-task-name">{ManageString}</p></div>
        <IconButton icon={ToRightIcon} disabled={blockLast} onClick={ShowNextMonth}/>
        {:else if type == 'week'}
        <IconButton icon={ToLeftIcon} disabled={blockLast} onClick={ShowLastWeek}/>
        <div class="managestring {type === 'mini' ? 'mini' : ''}"><p class="p-task-name">{ManageString}</p></div>
        <IconButton icon={ToRightIcon} disabled={blockLast} onClick={ShowNextWeek}/>
        {/if}
    </div>
    <div class="week-days">
        {#each weekDays as day}
            <div class="week-day {type === 'mini' ? 'mini' : ''}">
                <p class="{type == 'mini' ? 'p-task-name' : 'p-bold'}">{day}</p>
            </div>
        {/each}
    </div>
    <div class="dates {type === 'week' ? 'week' : ''}">
        {#if type === 'week'}
        {#each WeekList as date}
        {#key WeekList}
        <div class="day"><DateComponent type={type} {date} selectedDate={SelectedDate} on:SendDate={GetDate}/></div>
        {/key}
        {/each}
        {:else}
        {#if emptyDays > 0}
            <div class="empty" style="grid-column: span {emptyDays};"></div>
        {/if}
        {#each MonthList as date}
        {#key MonthList}
        <div class="day {type === 'mini' ? 'mini' : ''}"><DateComponent type={type} {date} selectedDate={SelectedDate} on:SendDate={GetDate}/></div>
        {/key}
        {/each}
        {/if}
    </div>
</div>