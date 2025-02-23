<script>
    import ChildItem from "./childItem.svelte";
    import IconButton from "../iconButton.svelte";
    import EditItem from "./EditItem.svelte";
    const titleText = 'список пакупок';
    const editIcon = '/icons/edit_icon.svg';
    const toBottomIcon = '/icons/tobottom_icon.svg';
    const torightIcon = '/icons/toright_icon.svg';
    const dotsIcon = '/icons/dots_icon.svg';
    let isExpanded = false;

    let editor = false;
    function toggle() {
        isExpanded = !isExpanded;
    }
    function editBlock(){
        editor = !editor;
    }
    

    let header = 'Редактировать';
    let name = 'Foo';
    let desc = 'Nooooo'
    let date;
    let hours = '2';
    let minutes = '22';
    let priority = 'middle';
    let user = 1;
    let status = 'archived';
</script>

<style>
    .contItem {
        overflow: hidden;
        display: grid;
        grid-template-columns: 0.7fr 2.3fr 0.3fr;
        grid-template-rows: auto;
        gap: 0px 0px;
        grid-auto-flow: row;
        grid-template-areas:
            "status title edit"
            "status desc edit";
        border-radius: 8px; 
        background-color: #eceff1; 
        margin: 5px;
        width: 500px;
    }
    .status { 
        grid-area: status;
        display: flex;
        justify-content:center;
        align-items: center;
        background-color: aquamarine;
    }
    .time{
        margin-left: 5px;
        font-size: 12px;
        font-weight: 400;
    }
    .title { 
        grid-area: title;
        margin: 2px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .title p {
        font-size: 14px;
        font-weight: 600;
    }
    .toggle-icon {
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        width: 24px;
        height: 24px;
        margin-left: 10px;
    }
    .desc { 
        grid-area: desc;
        display: flex;
        justify-content: flex-start;
        max-height: 0;
        height: fit-content;
        transition: max-height 0.5s linear;
    }
    .desc.expanded {
        overflow: hidden;
        max-height: 1000px;
        transition: max-height 0.5s linear;
    }
    .edit { 
        grid-area: edit;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>

{#if editor}
<EditItem 
header={header} 
name={name} 
desc={desc} 
date={date} 
hours={hours} 
minutes ={minutes}
priority = {priority}
user = {user}
status = {status}>
</EditItem>
{/if}

<div class="contItem">
    <div class="status">
        <div class='time'><p>17:40-18:30</p></div>
        <IconButton icon={dotsIcon}></IconButton>
    </div>
    <div class="title">
        <div>
            <p>{titleText}</p>
        </div>
        <button class="toggle-icon" on:click={toggle}>
            <img src={isExpanded ? toBottomIcon : torightIcon} alt="Toggle" />
        </button>
    </div>
    <div class="desc {isExpanded ? 'expanded' : ''}">
        <ul>
            <ChildItem></ChildItem>
        </ul>
    </div>
    <div class="edit">
        <IconButton icon={editIcon} onClick={editBlock}></IconButton>
    </div>
</div>