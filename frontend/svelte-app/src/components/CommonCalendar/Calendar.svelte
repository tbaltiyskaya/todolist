<script>
    import DateComponent from "./Date.svelte";
    const ToRightIcon = "icons/toright_icon.svg";
    const ToLeftIcon = "icons/toleft_icon.svg"
    const monthNames = [
        "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
    ];
    const weekDays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]


    let blockNext = false;
    let blockLast = false;
    export let SelectedDate = new Date();
    let emptyDays = 0;
    let currentMonth = SelectedDate.getMonth();
    let currentYear = SelectedDate.getFullYear();
    let MonthList = [];
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
    function DateSelect(event) {
        SelectedDate = event.detail;
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
    generateMonth();

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
</script>

<style>
    .calendar{
        width: 360px;
        height: 360px;
        padding: 10px 10px;
        box-shadow: rgba(0, 0, 0, 0.18) 0px 2px 4px;
        background-color: #eceff1;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        justify-content:start;
        align-items: center;
    }
    .manage{
        width: 250px;
        height: fit-content;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
    .week{
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: center;
    }
    .week-day{
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 8px 8px;
        width: 26px;
        height: 26px;
    }
    .week-day p{
        font-size: 20px;
        font-weight: 400;
    }
    button:active img{
        opacity: 0.4;
    }
    button img{
        width: 24px;
        height: 24px;
    }
    .dates{
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        grid-template-rows: repeat(6, 1fr);
    }
    .empty {
        grid-column: span 1;
    }
</style>

<div class="calendar">
    <div class="manage">
        <button id="last" disabled={blockLast} on:click={ShowLastMonth}>
            <img src= {ToLeftIcon} alt="Last">
        </button>
	        <p>{ManageString}</p>
        <button id="next" disabled={blockNext} on:click={ShowNextMonth}>
            <img src= {ToRightIcon} alt="Next">
        </button>
    </div>
    <div class="week">
        {#each weekDays as day}
            <div class="week-day"><p>{day}</p></div>
        {/each}
    </div>
    <div class="dates">
        {#if emptyDays > 0}
            <div class="empty" style="grid-column: span {emptyDays};"></div>
        {/if}
        {#each MonthList as date}
            <DateComponent {date} selectedDate={SelectedDate} on:dateClick={DateSelect}/>
        {/each}
    </div>
</div>