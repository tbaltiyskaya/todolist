<script>
    import IconButton from "../Buttons/iconButton.svelte";
    import EditStatus from "../Editor/EditStatus.svelte";
    import EditTask from "../Editor/EditTask.svelte";
    import UnzipTask from "../Editor/UnzipTask.svelte";
    const API_URL = 'http://127.0.0.1:5000';

    
    let list_datetype;
    let list_grouptype;
    export let task_id;
    export let watcher_id;

    let loading = false;

    let timed = true;
    let desced = true;
    let status_color = 'transparent';
    let priority_color = 'transparent';

    let author = { username: ''};
    let executor = { username: ''};

    let show_desc = false;

    let task_editor = false;
    let status_editor = false;

    const StatusIcon = '/icons/dots_icon.svg';
    const ToRightIcon = '/icons/toright_icon.svg';
    const ToBottomIcon = '/icons/tobottom_icon.svg';
    const EditIcon = '/icons/edit_icon.svg';
    const ArchiveIcon = '/icons/archive_icon.svg';
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    function SendUpdates(){
        dispatch('SendUpdates', data);
    }

    let task_props = {
        'list': 0,
        'author': 0,
        'executor': 0,
        'name': '',
        'desc': '',
        'date': '',
        'time': '',
        'priority': -1,
        'status': -1
    }

    let list_id = task_props.list;

    function ShowDesc(){
        show_desc = !show_desc;
    }

    function TaskEdit(){
        task_editor = true;
    }

    function StatusEdit(){
        status_editor = true;
    }

    function StatusColor(){
        if(task_props.status == 1){
            status_color = '#ffadad';
        }
        else if(task_props.status == 2){
            status_color = '#fdffb6';
        }
        else if(task_props.status == 3){
            status_color = '#caffbf';
        }
        else if(task_props.status == 4){
            status_color = '#edf2fa';
        }
        console.log('STATUS COLOR ', status_color);
    }

    function PriorityColor(){
        if(task_props.priority == 1){
            priority_color = '#ffadad';
        }
        else if(task_props.priority == 2){
            priority_color = '#fdffb6';
        }
        else if(task_props.priority == 3){
            priority_color = '#caffbf';
        }
    }


    function GetNewStatus(event){
        task_props.status = event.detail.status;
        StatusColor();
    }

    async function CheckList() {
        const response = await fetch(`${API_URL}/check_list`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ list_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
        }
        const data = await response.json();
        if (data.status === 'success') {
            const { 
                list_datetype: fetcheddatetype,
                list_grouptype: fetchedgrouptype,
            } = data.data;
            list_datetype = fetcheddatetype;
            list_grouptype = fetchedgrouptype;
        } else {
            console.log('ERROR TASK');
        }
    }

    async function ShowUser(user_id, user) {
        const response = await fetch(`${API_URL}/show_user_by_id`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            return;
        }
        const data = await response.json();
        if (data.status === 'success') {
            const { username: fetchedUsername, email: fetchedEmail } = data.data;
            user.username = fetchedUsername;
        } else {
            console.log('ERROR');
        }
    }
    

    async function ShowTask() {
        const response = await fetch(`${API_URL}/show_task`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
        }
        const data = await response.json();
        if (data.status === 'success') {
            const { 
                list: fetchedlist,
                author: fetchedauthor,
                executor: fetchedexecutor,
                name: fetchedname,
                desc: fetcheddesc, 
                date: fetcheddate, 
                time: fetchedtime, 
                priority: fetchedpriority, 
                status: fetchedstatus
            } = data.data;
            task_props.list = fetchedlist;
            list_id = fetchedlist;
            task_props.author = fetchedauthor;
            task_props.executor = fetchedexecutor;
            task_props.name = fetchedname;
            task_props.desc = fetcheddesc;
            task_props.date = fetcheddate;
            task_props.time = fetchedtime;
            task_props.priority = fetchedpriority;
            task_props.status = fetchedstatus;
            console.log('TASK: ', task_props);
            if(task_props.status != 0){
                await ShowUser(task_props.author, author);
                await ShowUser (task_props.executor, executor);
                await CheckList();
                StatusColor();
                PriorityColor();
                loading = true;
            }
            else{
                loading = true;
            }
        } else {
            console.log('ERROR TASK');
        }
    }


    async function CanceltaskEdit(){
        task_editor = false;
        await ShowTask();
        SendUpdates();
    }

    async function CancelStatusEdit(){
        status_editor = false;
        await ShowTask();
        SendUpdates();
    }

    ShowTask();
    
</script>

{#key loading}
<div class="task-container">
    <div class="change_status {status_editor ? 'active' : ''}">
        {#if task_props.status == 0}
        {#if status_editor}
        <UnzipTask task_id={task_id} author_id={watcher_id} on:cancel={CancelStatusEdit}/>
        {/if}
        {:else}
        {#if status_editor}
        <EditStatus grouptype={list_grouptype} task_id={task_id} task_status={task_props.status} 
        watcher_id={watcher_id} author_id={task_props.author} executor_id={task_props.executor}
        on:cancel={CancelStatusEdit} on:SendNewStatus={GetNewStatus}/>
        {/if}
        {/if}
    </div>
    <div class="task">
        <div class="status" style="background-color: {status_color};">
            {#if watcher_id == task_props.author || watcher_id == task_props.executor}
            {#if task_props.status == 0}
            <div>
                <IconButton icon={ArchiveIcon} onClick={StatusEdit}/>
            </div>
            {:else}
            <div>
                <IconButton icon={StatusIcon} onClick={StatusEdit}/>
            </div>
            {/if}
            {/if}
            {#if timed}
            <div class="time"><p class="p-task-desc">{task_props.time}</p></div>
            {/if}
        </div>
    
        <div class='naming'>
            <div class="user">
                {#if task_props.author != task_props.executor}
                    {#if watcher_id == task_props.author}
                        <div><p class="p-task-small">Кому: {executor.username}</p></div>
                    {:else if watcher_id == task_props.executor}
                        <div><p class="p-task-small">От: {author.username}</p></div>
                    {:else}
                        <div><p class="p-task-small">От: {author.username}</p></div>
                        <div><p class="p-task-small">Кому: {executor.username}</p></div>
                    {/if}
                {/if}
                </div>
            <div class="name">
                <div><p class="p-task-name">{task_props.name}</p></div>
                {#if desced}
                <div>
                {#if show_desc}
                <IconButton icon={ToBottomIcon} onClick={ShowDesc}/>
                {:else}
                <IconButton icon={ToRightIcon} onClick={ShowDesc}/>
                {/if}
                </div>
                {/if}
            </div>
            {#if show_desc}
            <div class="desc">
                <p class="p-task-desc">{task_props.desc}</p>
            </div>
            {/if}
        </div>
        <div class="panel" style="background-color: {priority_color};">
            {#if task_props.status != 0}
            {#if task_props.author == watcher_id}
            <IconButton icon={EditIcon} onClick={TaskEdit}/>
            {/if}
            {/if}
        </div>
    </div>
</div>
{#if task_editor}
        <EditTask task_id={task_id} task_list={task_props.list} task_author={task_props.author} task_executor={task_props.executor}
        task_name={task_props.name} task_desc={task_props.desc} task_date={task_props.date} task_time={task_props.time}
        task_priority={task_props.priority} list_datetype={list_datetype} list_grouptype={list_grouptype}
        on:cancel={CanceltaskEdit}/>
{/if}
{/key}



<style>
    .task-container{
        position: relative;
    }
    .change_status{
        display: none;
        width: 0;
        height: 0;
    }
    .change_status.active{
        display: flex;
        position: absolute;
        top: 10px; left: -150px;
        width: fit-content;
        height: fit-content;
    }
    .task{
        background-color: white;
        width: 500px;
        height: fit-content;
        box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 2px, rgba(0, 0, 0, 0.23) 0px 1px 2px;
        border-radius: 4px; margin: 4px;
        display: flex; flex-direction: row;
        justify-content: space-between; align-items: center;
    }
    .task > div{
        display: flex;
        align-items: center;
    }
    .status{
        border-radius: 0 8px 8px 0;
        justify-content: center;
        height: 100%;
    }
    .status > div{
        display: flex; justify-content: center;
        align-items: center;
    }
    .time{
        margin: 0 10px 0 0;
        
    }
    .naming{
        border-left: 1px solid #c5c9cf;
        border-right: 1px solid #c5c9cf;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: center;
    }
    .naming > div{
        margin-bottom: 4px;
        width: 100%;
    }
    .panel{
        border-radius:  8px 0 0 8px;
        height: 100%;
        width: 30px;
        display: flex;
        justify-content: center;
    }
    .name{
        height: fit-content;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    .user{
        height: 15px;
        display: flex;
        flex-direction: row;
        justify-content: start; align-items: center;
    }
    .user > div{
        margin: 4px 6px 0 0;
    }
    .desc{
        width: 100%;
        border-top: 1px solid #c5c9cf;
        height: fit-content;
        display: flex; justify-content: start;
        align-items: center;
    }
    
</style>