<script>
    export let hours;
    export let minutes;

    const hoursOptions = Array.from({length: 24}, (_, i) => i);
    const minutesOptions = Array.from({length: 60}, (_, i) => i);
    
    function padNumber(num) {
        return num.toString().padStart(2, '0');
    }
    
    function handleHoursChange(event) {
        hours = parseInt(event.target.value);
    }
    
    function handleMinutesChange(event) {
        minutes = parseInt(event.target.value);
    }
</script>

<div class='time_selector'>
    <select size="8" 
        class='hours' 
        bind:value={hours}
        on:change={handleHoursChange}>
        {#each hoursOptions as hour}
            <option value={hour}>{padNumber(hour)}</option>
        {/each}
    </select>
    
    <select size="8"
        class='minutes' 
        bind:value={minutes}
        on:change={handleMinutesChange}
    >
        {#each minutesOptions as minute}
            <option value={minute}>{padNumber(minute)}</option>
        {/each}
    </select>
</div>

<style>
.time_selector {
    display: flex;
    align-items: center;
    border: none;
}
.hours,
.minutes {
    width: 60px;
    padding: 4px;
    border: none;
    font-size: 14px;
    appearance: none;
}

.hours:focus,
.minutes:focus {
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
}
</style>