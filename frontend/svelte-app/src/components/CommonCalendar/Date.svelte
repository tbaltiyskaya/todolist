<script>
    import { createEventDispatcher } from 'svelte';
    export let date;
    export let selectedDate;

    const buttonDispatch = createEventDispatcher();

    let day = date.getDate();

    function ButtonClick(){
        buttonDispatch('dateClick', date);
        console.log(selectedDate);
    }
    

</script>
<style>
    .date{
        border-radius: 4px;
        margin: 8px 8px;
        width: 26px;
        height: 26px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    button{
        width: 100%;
        height: 100%; 
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: transparent;
    }
    button.clicked{
        background-color: aqua;
    }
    .date > button p{
        color: #000000;
    }
</style>

<div class="date">
    <button class:clicked={date === selectedDate} on:click={ButtonClick}><p>{day}</p></button>
</div>