<script>
    import { createEventDispatcher } from 'svelte';
    import Friends from '../Users/Friends.svelte';
    import IconButton from '../Buttons/iconButton.svelte';
    const dispatch = createEventDispatcher();
    const API_URL = 'http://127.0.0.1:5000';
    
    const CloseIcon = '/icons/close_icon.svg';
    
    export let list_id;
    export let author_id;
    
    function Cancel(){
        dispatch('cancel');
    }

</script>

<div class="creator">
    <div class="buttons">
        <IconButton icon={CloseIcon} onClick={Cancel}/>
    </div>
    <div class='block-header'><p>Добавить пользователей</p></div>
    <div class="data">
        <Friends watcher_id={author_id} subject_id={list_id} operation='member_create'/>
    </div>
</div>


<style>
    .creator{
        position: absolute;
        top:10%; left: 40%;
        z-index: 18;
        width: 400px;height: fit-content;
        padding: 10px; border-radius: 8px;
        background-color: white;
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
        display: flex; flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
    .creator > div{
        width: 90%;
        margin: 4px;
        height: fit-content; 
    }
    .block-header{
        display: flex; justify-content: center; align-items: center;
        width: fit-content; height: 30px;
    }
    .block-header p{
        font-size: 16px;
        font-weight: 600;
    }
    .data{
        height: fit-content;
        display: flex; flex-direction: column;
        justify-content: start;
        align-items: center;
    }
    .buttons{
        height: fit-content;
        display: flex;
        flex-direction: row;
        justify-content: end;
        align-items: center;
    }
</style>