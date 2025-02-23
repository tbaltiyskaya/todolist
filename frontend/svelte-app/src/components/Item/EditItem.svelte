<script>
    import Calendar from "../CommonCalendar/Calendar.svelte";
    import IconButton from "../iconButton.svelte";
    import TimeSelector from "../CommonCalendar/TimeSelector.svelte";
    import User from "../notices/User.svelte";
    const save = '../icons/save_icon.svg';
    const close = '../icons/close_icon.svg';
    const calendar = '../icons/calendar_icon.svg';
    const timer  = '../icons/time_icon.svg';
    const toBottomIcon = '/icons/tobottom_icon.svg';
    const torightIcon = '/icons/toright_icon.svg';

    export let header;
    export let name;
    export let desc;
    export let date;
    export let hours;
    export let minutes;
    export let priority;

    let users_id = [1,2,3,4];

    let isExpanded = false;
    $: tempName = name;
    $: tempDesc = desc;

    $: tempDate = date;
    $: calDate = tempDate;

    $:tempHours = hours;
    $:tempMinutes = minutes;
    $:selHours = tempHours;
    $:selMinutes = tempMinutes;

    $:tempPriority = priority;

    let tempUser;

    
    let dateChoose = false;
    let timeChoose = false;


    function saveChanges(){
      try {
        name = tempName;
        desc = tempDesc;
        date = tempDate;
        console.log('Сохраненные данные:', { name, desc, date});
    } catch (error) {
        console.error('Ошибка при сохранении:', error);
    }
    }

    function cancelChanges() {
    try {
        dateChoose = false;
        tempName = name;
        tempDesc = desc;
        console.log('Несохраненные данные:', { name, desc });
    } catch (error) {
        console.error('Ошибка при отмене изменений:', error);
    }
}

function openChooseDate() {
  dateChoose = !dateChoose;
  console.log(dateChoose);}

function closeChooseDate(){
  dateChoose = false;}

function closeChooseTime(){
  timeChoose = false;
}

function saveChooseDate(){
  tempDate = calDate;
  console.log('tempdate = ', tempDate);
  dateChoose = false;
}

function saveChooseTime(){
  tempHours = selHours;
  tempMinutes = selMinutes;
  timeChoose = false;
}

function openChooseTime(){
  timeChoose = !timeChoose;
}

function changePriority(level) {
  tempPriority = level;
}
    
function getButtonColor(level) {
  if (tempPriority === 'low') {
    if (level === 'low') {return '#a5d6a7'; }
      return 'transparent';
  } 
  else if (tempPriority === 'middle') {
   if (level === 'high') { return 'transparent';}
    return '#fff9c4';}
  return '#ffcdd2';
}

function toggle() {
    isExpanded = !isExpanded;
    console.log('Состояние isExpanded:', isExpanded);
    console.log('Список пользователей:', users_id);
}

function selectUser (UserID) {
        tempUser  = UserID;
        moveToFirst(users_id, UserID);
        isExpanded = false;
        console.log('Выбранный пользователь:', tempUser);
        console.log('Обновленный список:', users_id);
}

function moveToFirst(arr, index) {
    if (index > 0) {
        const element = arr.splice(index, 1)[0];
        arr.unshift(element);
    }
}

</script>
<style>
    .ItemForm{
        width: 600px;
        border-radius: 8px;
        height: fit-content;
        padding: 10px 20px 20px;
        background-color: #f8fafb;
        box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 8px;
        display: grid;
        grid-template-columns: 1.5fr 1.4fr 0.6fr;
        grid-template-rows: 0.6fr 2fr 0.8fr 0.7fr;
        gap: 0px 0px;
        grid-auto-flow: row;
        grid-template-areas:
            "header header close"
            "text text text"
            "prop prop prop"
            "to to save";
    }

    .close { grid-area: close; display: flex; justify-content:end; align-items: center;}
    .calendar{
      width: 380px;
      position: absolute;
      top:50px;
      z-index: 12;
    }
    .timer{
      box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
      border-radius: 4px;
      background-color: white;
      position: absolute;
      display: flex;
      justify-content: center; align-items: start;
      z-index: 16;
      top:50px;
      width: 180px;
    }
    .close_calendar{
      position: absolute;
      left: 0;
      top:0;
      z-index: 16;
    }
    .save_calendar{
      position: absolute;
      top: 0;
      right: 0;
      z-index: 16;
    }
    .save { grid-area: save; display: flex; justify-content:end; align-items: center;}

    .toggle-icon {
        z-index: 12;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        width: 24px;
        height: 24px;
        margin-left: 10px;
    }

    .to { 
      grid-area: to;
      position: relative;
      display: flex; flex-direction: row; justify-content: space-between;
      align-items: center;
      width: 330px;
      gap: 5px;
      height: 35px;
      font-size: 14px;
    }
    .user_selector{
      position: absolute; left: 100px; top: 0;
      padding: 4px;
      display: flex; flex-direction: column;
      align-items: center;
      z-index: 12;
      width: 210px;
      height: fit-content;
      max-height: 58px;
      overflow: hidden;
      transition: max-height 0.5s linear;
    }
    .user_selector.expanded {
        max-height: 1000px;
        transition: max-height 0.5s linear;
    }

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
.prop > div{
  display: flex; 
  height: 60px;
}

.date { grid-area: date;  align-items: center; position: relative; }

.time { grid-area: time; align-items: center; position: relative;
}

.priority { 
  grid-area: priority; padding: 4px; 
  flex-direction: column; align-items: center; justify-content: start;
 }
.scale{
  display: flex; flex-direction: row;
  border: 1px solid black;
}
.scale > div{
  width: 60px;
  height: 12px;
  display: flex;
}
.scale > div button{
  width: 60px;
  height: 12px;
  display: flex;
  justify-content: center; align-items: center;
}
.scale div p{
  font-size: 10px;
}
</style>

<div class="ItemForm">
    <div class="close"><IconButton icon={close} onClick={cancelChanges}></IconButton></div>
    <div class="save"><IconButton icon={save} onClick={saveChanges}></IconButton></div>
    <div class="to">
      <p>Получатель:</p>
      <div class:user_selector= {true} class:expanded={isExpanded}>
        {#each users_id as userID}
            <User
                UserID={userID}
                on:click={() => selectUser(userID)}
            />
        {/each}
      </div>
      <button class="toggle-icon" on:click={toggle}>
        <img src={isExpanded ? toBottomIcon : torightIcon} alt="Toggle" />
      </button>
    </div>
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
        <IconButton icon={calendar} onClick={openChooseDate}></IconButton>
        <p>{tempDate}</p>
        {#if dateChoose}
        <div class='calendar'>
          <div class='close_calendar'><IconButton icon={close} onClick={closeChooseDate}></IconButton></div>
          <div class='save_calendar'><IconButton icon={save} onClick={saveChooseDate}></IconButton></div>
          <Calendar bind:SelectedDate={calDate}>
          </Calendar>
        </div>
        {/if}
      </div>
      <div class="time">
        <IconButton icon={timer} onClick={openChooseTime}></IconButton>
        <p>{tempHours}:{tempMinutes}</p>
        {#if timeChoose}
        <div class='timer'>
          <div class='close_calendar'><IconButton icon={close} onClick={closeChooseTime}></IconButton></div>
          <div class='save_calendar'><IconButton icon={save} onClick={saveChooseTime}></IconButton></div>
          <TimeSelector bind:hours={selHours} bind:minutes={selMinutes}></TimeSelector>
        </div>
        {/if}
      </div>
      <div class="priority">
        <p>Приоритет</p>
        <div class='scale'>
          <div><button class='low' on:click={() => changePriority('low')}
            style={`background-color: ${getButtonColor('low')}`}><p>Низкий</p></button></div>
          <div><button class='middle' on:click={() => changePriority('middle')}
            style={`background-color: ${getButtonColor('middle')}`}><p>Средний</p></button></div>
          <div><button class='high' on:click={() => changePriority('high')}
            style={`background-color: ${getButtonColor('high')}`}><p>Высокий</p></button></div>
        </div>
      </div>
    </div>
  </div>
