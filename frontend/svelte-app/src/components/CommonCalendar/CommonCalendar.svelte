<script>
import ToDoItem from "../Item/ToDoItem.svelte";
import Calendar from "./Calendar.svelte";
import DayItems from "../Item/DayItems.svelte";

let date;
</script>
<style>
    .common-calendar{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
    }
    .common-calendar > div{
        display: flex;
        justify-content: center;
        width: 450px;
        height: 500px;
    }
</style>

<div class="common-calendar">
    <div class="calendar-block">
        <Calendar bind:SelectedDate = {date}/>
    </div>
    <div class="day-items">
        <DayItems {date}/>
    </div>
</div>
