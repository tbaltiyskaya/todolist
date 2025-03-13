<script>
    import IconButton from "../Buttons/iconButton.svelte";
    const SaveIcon = '/icons/save_icon.svg';
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    let hours = '';
    let minutes = '';

    function SetHour(hour){
        hours = hour;
    }
    function SetMinute(minute){
        minutes = minute;
    }
    function SendTimeToPage(){
        const data = {'selected_time': hours + ":" + minutes};
        dispatch('SendTimeToPage', data);
    }

    $:selected_time = (hours != '' && minutes != '');

    const hoursOptions = Array.from({length: 24}, (_, i) => String(i).padStart(2, '0'));
    const minutesOptions = Array.from({length: 60}, (_, i) => String(i).padStart(2, '0'));

</script>

<div class="container">
    <div>
        <IconButton icon={SaveIcon} disabled={!selected_time} onClick={SendTimeToPage}/>
    </div>
    <div class='time_selector'>
        <div class='hours'>
            {#each hoursOptions as hour}
            <div class="option {hours == hour ? 'active' : ''}">
                <button on:click={() => SetHour(hour)}><p class="p-task-desc">{hour}</p></button>
            </div>
            {/each}
        </div>
        <div class='minutes'>
            {#each minutesOptions as minute}
            <div class="option {minutes == minute ? 'active' : ''}">
                <button on:click={() => SetMinute(minute)}><p class="p-task-desc">{minute}</p></button>
            </div>
            {/each}
        </div>
    </div>
</div>


<style>
.container{
    background-color: white;
    border: 1px solid #c5c9cf;
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
}
.container > div{
    margin: 0 5px 5px;
}
.time_selector {
    display: flex;
    align-items: center;
    border: none;
}
.hours,
.minutes {
    width: 22px;
    height: 80px;
    overflow-y: scroll;
    background-color: white;
    border: 1px solid #c5c9cf;
}
.hours::-webkit-scrollbar,
.minutes::-webkit-scrollbar{
    width: 0px;
}
.option{
    width: 100%;
    height: 14px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.option button{
    height: 100%;
    width: 100%;
}
.option:hover{
    background-color: #c1d3fe;
}
.option.active{
    background-color: #abc4ff;
}

</style>