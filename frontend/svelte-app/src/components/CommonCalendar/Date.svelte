<script>
    import { createEventDispatcher } from 'svelte';
    export let date;
    export let selectedDate;
    export let type;

    const dispatch = createEventDispatcher();

    let day = date.getDate();

    function SendDate(){
        const data = {'selected_date': date};
        dispatch('SendDate', data);
    }
    

</script>
<style>
    .day{
        width: 100%;
        height: 100%; 
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: transparent;
    }
    .day:hover{
        background-color: #ccdbfd;
    }
    .day.active{
        background-color: #c1d3fe;
    }
</style>


<button class="day {date.getTime() === selectedDate.getTime() ? 'active' : ''}" on:click={SendDate}>
    {#if type === 'mini'}
    <p class="p-task-desc">{day}</p>
    {:else}
    <p class="p-classic">{day}</p>
    {/if}
</button>