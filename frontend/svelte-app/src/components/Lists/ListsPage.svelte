<script>
    export let user_id;

    import LargeButton from "../Buttons/LargeButton.svelte";
    import ListCover from "./ListCover.svelte";
    import CreateList from "../Creator/CreateList.svelte";
    import List from "./List.svelte";
    const AddIcon = '/icons/plus_icon.svg';
    const API_URL = 'http://127.0.0.1:5000';

    let loading = false;
    let adding_list = false;
    let filter;

    let lists_id = [];

    function FilterList(type){
        loading = false;
        filter = type;
        if(type == 'all'){
            ShowAllLists();
        }
        else if(type == 'own'){
            ShowOwnLists();
        }
        else if(type == 'group'){
            ShowGroupLists();
        }
        else if(type == 'author'){
            ShowAuthorLists();
        }
    }

    function AddList(){
        adding_list = true;
    }

    function CancelAddList(){
        adding_list = false;
    }

    async function ShowAllLists() {
        const response = await fetch(`${API_URL}/show_all_lists`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id})
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            console.log('Нет соединения')
        }
        const data = await response.json();
        if (data.status === 'success') {
            const listIds = data.data;
            lists_id = [];
            lists_id = listIds;
            loading = true;
        } 
        else {
            console.log('ERROR');
        }
    }

    async function ShowOwnLists() {
        const response = await fetch(`${API_URL}/show_own_lists`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id})
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            console.log('Нет соединения')
        }
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS LISTS OWN');

            const listIds = data.data;
            lists_id = [];
            lists_id = listIds;
            loading = true;
            console.log('lists_id = ', lists_id);
        } 
        else {
            console.log('ERROR');
        }
    }


    async function ShowGroupLists() {
        const response = await fetch(`${API_URL}/show_group_lists`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id})
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            console.log('Нет соединения')
        }
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS LISTS GROUP');

            const listIds = data.data;
            lists_id = [];
            lists_id = listIds;
            loading = true;
            console.log('lists_id = ', lists_id);
        } 
        else {
            console.log('ERROR');
        }
    }


    async function ShowAuthorLists() {
        const response = await fetch(`${API_URL}/show_author_lists`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id})
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            console.log('Нет соединения')
        }
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            const listIds = data.data;
            lists_id = [];
            lists_id = listIds;
            loading = true;
            console.log(lists_id);
        } 
        else {
            console.log('ERROR');
        }
    }

    let is_selected = false;

    function CancelList(){
        is_selected = false;
    }

    let selected_list_data = {
            'list_id': 0, 
            'list_name': '', 
            'list_author': 0,
            'list_datetype': false,
            'list_grouptype': false
         };

    function ShowSelectedList(event){
        selected_list_data.list_id = event.detail.list_id;
        selected_list_data.list_name = event.detail.list_name;
        selected_list_data.list_author = event.detail.list_author;
        selected_list_data.list_datetype = event.detail.list_datetype;
        selected_list_data.list_grouptype = event.detail.list_grouptype;
        is_selected = true;
    }


    FilterList('all');
</script>
    
{#if !is_selected}
<div class="list-page">
    <div class="nav">
        <div class="filter">
            <div><button class="filter-btn {(filter === 'all') ? 'active': ''}" on:click|preventDefault={() => FilterList('all')}><p>Все</p></button></div>
            <div><button class="filter-btn {(filter === 'own') ? 'active': ''}" on:click|preventDefault={() => FilterList('own')}><p>Личные</p></button></div>
            <div><button class="filter-btn {(filter === 'group') ? 'active': ''}" on:click|preventDefault={() => FilterList('group')}><p>Групповые</p></button></div>
            <div><button class="filter-btn {(filter === 'author') ? 'active': ''}" on:click|preventDefault={() => FilterList('author')}><p>Управляемые</p></button></div>
        </div>
        <LargeButton icon={AddIcon} onClick={AddList} />
    </div>
    <div class='container'>
        {#if adding_list}
        <CreateList {user_id} on:cancel={CancelAddList}/>
        {/if}
        {#if loading}
            {#each lists_id as list_id}
                <ListCover {list_id} {user_id} on:ListSelect={ShowSelectedList} />
            {/each}    
        {/if}
    </div>
</div>
{:else}
<div class="selected-list">
    <List user_id={user_id} 
    list_id={selected_list_data.list_id}
    list_name={selected_list_data.list_name}
    list_author={selected_list_data.list_author}
    list_datetype={selected_list_data.list_datetype}
    list_grouptype={selected_list_data.list_grouptype} on:cancel={CancelList}/>
</div>
{/if}



<style>
    .selected-list{
        width: 100%;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .list-page{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: center;
    }
    .nav{
        width: 90%;
        height: 50px; margin: 5px 30px;
        display: flex;flex-direction: row;
        justify-content: space-between;align-items: center;
    } 
    .filter{
        display: flex;
        flex-direction: row;
        justify-content: center; align-items: center;
        width: fit-content;
    }
    .filter div{
        margin: 0 15px;
    }
    .filter-btn{
        display: flex; justify-content: center; align-items: center;
    }
    .filter-btn p{
        font-size: 16px;
        font-weight: 400;
    }
    .filter-btn.active p{
        font-weight: 500;
    }
    .container{
        width: 90%;
        height: 100%;
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: start;
        align-items: start;
        position: relative;
    }
</style>
