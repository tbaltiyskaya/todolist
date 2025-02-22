<script>
    import Calendar from "../CommonCalendar/Calendar.svelte";
    import IconButton from "../iconButton.svelte";
    const save = '../icons/save_icon.svg';
    const close = '../icons/close_icon.svg';
    const calendar = '../icons/calendar_icon.svg';
    const time  = '../icons/time_icon.svg';
    export let header;
    export let name;
    export let desc;
    export let date;

    $: tempName = name;
    $: tempDesc = desc;
    let dateChoose = false;

    function saveChanges(){
      try {
        // Обновляем значения
        name = tempName;
        desc = tempDesc;
        console.log('Сохраненные данные:', { name, desc });
    } catch (error) {
        console.error('Ошибка при сохранении:', error);
    }
    }

    function cancelChanges() {
    try {
        // Восстанавливаем исходные значения
        tempName = name;
        tempDesc = desc;
        console.log('Несохраненные данные:', { name, desc });
    } catch (error) {
        console.error('Ошибка при отмене изменений:', error);
    }
}

function openChooseDate() {
    try {
        console.log('calendar is opened');
        dateChoose = !dateChoose;
        console.log(dateChoose);
    } catch (error) {
        console.error('Ошибка при открытии календаря:', error);
    }
}

</script>
<style>
    .ItemForm{
        width: 600px;
        border-radius: 8px;
        height: fit-content;
        padding: 10px 20px 15px;
        background-color: #f8fafb;
        box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 8px;
        display: grid;
        grid-template-columns: 1.5fr 1.4fr 0.6fr;
        grid-template-rows: 0.6fr 2fr 0.8fr 0.6fr;
        gap: 0px 0px;
        grid-auto-flow: row;
        grid-template-areas:
            "header header close"
            "text text text"
            "prop prop prop"
            "from to save";
    }

    .close { grid-area: close; display: flex; justify-content:end; align-items: center;}
    .save { grid-area: save; display: flex; justify-content:end; align-items: center;}

    .from { grid-area: from; }
    .to { grid-area: to; }
    .header { grid-area: header; font-size: 22; font-weight: 600; padding-bottom: 10px;}

.text {  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
  gap: 10px 0px;
  grid-auto-flow: row;
  grid-template-areas:
    "name name name"
    "desc desc desc"
    "desc desc desc";
  grid-area: text;
}

.name {
    font-weight: 500;
    grid-area: name;
    align-items: flex-start;
    padding: 6px; border-radius: 8px;
    box-shadow: 0px 5px 10px 2px rgba(34, 60, 80, 0.2) inset;
}

.desc { 
    grid-area: desc;
    align-items: flex-start;
    padding: 6px; border-radius: 8px;
    box-shadow: 0px 5px 10px 2px rgba(34, 60, 80, 0.2) inset;
 }

.prop {  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
  gap: 0px 0px;
  grid-auto-flow: row;
  grid-template-areas:
    "date time priority"
    "date time priority"
    "date time priority";
  grid-area: prop;
}

.date { grid-area: date;  display: flex; align-items: center; position: relative; }

.time { grid-area: time;  display: flex; align-items: center;}

.priority { grid-area: priority; }
</style>

<div class="ItemForm">
    <div class="close"><IconButton icon={close} on:click={cancelChanges}></IconButton></div>
    <div class="save"><IconButton icon={save} on:click={saveChanges}></IconButton></div>
    <div class="from">from</div>
    <div class="to">to</div>
    <div class="header"><p>{header}</p></div>
    <div class="text">
      <div class="name" contenteditable="true"
      bind:innerHTML={tempName}
      on:input={e => tempName = e.target.innerHTML} placeholder="Введите имя"></div>
      <div class="desc"       contenteditable="true"
      bind:innerHTML={tempDesc}
      on:input={e => tempDesc = e.target.innerHTML}
      placeholder="Введите описание"></div>
    </div>
    <div class="prop">
      <div class="date">
        <IconButton icon={calendar} on:click={openChooseDate}></IconButton>
        {#if dateChoose}
        <Calendar bind:SelectedDate={date}/>
        {/if}
      </div>
      <div class="time"><IconButton icon={time}></IconButton></div>
      <div class="priority">middle</div>
    </div>
  </div>
