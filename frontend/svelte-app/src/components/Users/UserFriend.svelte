<script>
    export let user_id;
    export let watcher_id;
    export let subject_id;
    export let operation;

    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    import IconButton from "../Buttons/iconButton.svelte";
    import CreateFriend from "../Creator/CreateFriend.svelte";
    import CreateMember from "../Creator/CreateMember.svelte";
    import CreateExecutor from "../Creator/CreateExecutor.svelte";
    import DeleteFriend from "../Detelor/DeleteFriend.svelte";
    import DeleteMember from "../Detelor/DeleteMember.svelte";
    import User from "./User.svelte";

    
    const AddIcon = '/icons/plus_icon.svg';
    const DeleteIcon = '/icons/close_icon.svg';
    const SaveIcon = '/icons/save_icon.svg';

    let delete_friend = false;
    let create_friend = false;
    let delete_member = false;
    let create_member = false;
    let create_executor = false;

    let username;
    function GetUsername(event){
        username = event.detail.username;
    }

    function SendExecutor(){
        const data = {'executor_id': user_id, 'executor_name': username};
        dispatch('SendExecutor', data);
    }

    //Удалить из друзей
    function FriendDelete() {
        delete_friend = true;
    }

    function CancelFriendDelete(){
        delete_friend = false;
    }
    //Подружиться 
    function FriendCreate(){
        create_friend = true;
    }

    function CancelFriendCreate(){
        create_friend = false;
    }

    function MemberCreate(){
        create_member = true;
    }

    function CancelMemberCreate(){
        create_member = false;
    }

    function MemberDelete(){
        delete_member = true;
    }

    function CancelMemberDelete(){
        delete_member = false;
    }

    function ExecutorCreate(){
        create_executor = true;
    }

    function CancelExecutorCreate(){
        create_executor = false;
    }
</script>

<div class='user-friend'>
    <div>
        <User {user_id} on:SendUsername={GetUsername}/>
    </div>
    <div>
        {#if operation == 'friend_create'}
            <IconButton icon={AddIcon} onClick={FriendCreate}/>
        {:else if operation == 'friend_delete'}
            <IconButton icon={DeleteIcon} onClick={FriendDelete}/>
        {:else if operation == 'member_create'}
            <IconButton icon={AddIcon} onClick={MemberCreate}/>
        {:else if operation == 'member_delete'}
            <IconButton icon={DeleteIcon} onClick={MemberDelete}/>
        {:else if operation == 'executor_create'}
            <IconButton icon={SaveIcon} onClick={SendExecutor}/>
        {/if}
    </div>
    {#if create_friend}
        <CreateFriend user_id={watcher_id} friend_id={user_id} friend_name={username} on:cancel={CancelFriendCreate}/>
    {/if}
    {#if delete_friend}
        <DeleteFriend user_id={watcher_id} friend_id={user_id} friend_name={username} on:cancel={CancelFriendDelete}/>
    {/if}
    {#if create_member}
        <CreateMember author_id={watcher_id} member_id={user_id} list_id={subject_id} member_name={username} on:cancel={CancelMemberCreate}/>
    {/if}
    {#if delete_member}
        <DeleteMember author_id={watcher_id} member_id={user_id} list_id={subject_id} member_name={username} on:cancel={CancelMemberDelete}/>
    {/if}
    
</div>


<style>
    .user-friend{
        background-color: white;
        box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 2px, rgba(0, 0, 0, 0.23) 0px 1px 2px;
        border-radius: 4px; margin: 4px;
        width: fit-content;height: fit-content;
        display: flex; flex-direction: row;
        justify-content: center; align-items: center;
    }
    .user-friend:hover{
        background-color: #eff3f8;
    }
    .user-friend > div{
        width: fit-content; height: fit-content;margin: 5px;
        display: flex;justify-content: center; align-items: center;
    }
</style>