<script>
    export let user_id;

    let notice_friend_ids = [];
    let notice_list_ids = [];
    $:show = 'calendar';
    import User from "./User.svelte";
    import UserMenu from "./UserMenu.svelte";
    import CommonCalendar from "../CommonCalendar/CommonCalendar.svelte";
    import ListsPage from "../Lists/ListsPage.svelte";
    import Archive from "../Archives/Archive.svelte";
    import NoticeFriend from "../Creator/NoticeFriend.svelte";
    import NoticeList from "../Creator/NoticeList.svelte";

    const API_URL = 'http://127.0.0.1:5000';

    function ShowPage(button){
        if(button == 'calendar'){
            show = 'calendar';
        }
        else if(button == 'lists'){
            show = 'lists';
        }
        else if(button == 'archive'){
            show = 'archive';
        }
    }

    async function GetFriendNotices() {
        const response = await fetch(`${API_URL}/show_friend_notices`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
        }
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS NOTICES');
            notice_friend_ids = [];
            const notices = data.data;
            notice_friend_ids = notices;
            console.log('notice_ids = ', notice_friend_ids)
        } else {
            console.log('ERROR');
        }
    }

    async function GetListNotices() {
        const response = await fetch(`${API_URL}/show_list_notices`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
        }
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS NOTICES');
            notice_list_ids = [];
            const notices = data.data;
            notice_list_ids = notices;
            console.log('notice_ids = ', notice_list_ids)
        } else {
            console.log('ERROR');
        }
    }

    function EditFriendsNotices(event){
        let notice = event.detail.notice_id;
        notice_friend_ids = notice_friend_ids.filter(num => num !== notice);
        GetFriendNotices();
    }

    function EditListsNotices(event){
        let notice = event.detail.notice_id;
        notice_list_ids = notice_list_ids.filter(num => num !== notice);
        GetListNotices();
    }

    GetFriendNotices();
    GetListNotices();
</script>

<main>
    <div class="user-menu"><UserMenu {user_id}></UserMenu></div>
    <div class="user-page">
        <div class='nav'>
            <div><button class="filter-btn {show === 'calendar' ? 'active' : ''}" on:click={() => ShowPage('calendar')}><p>Календарь</p></button></div>
            <div><button class="filter-btn {show === 'lists' ? 'active' : ''}" on:click={() => ShowPage('lists')}><p>Листы</p></button></div>
            <div><button class="filter-btn {show === 'archive' ? 'active' : ''}" on:click={() => ShowPage('archive')}><p>Архив</p></button></div>
        </div>
        <div class='show'>
            {#if show == 'calendar'}
            <CommonCalendar {user_id}/>
            {:else if show == 'lists'}
            <ListsPage {user_id} />
            {:else if show == 'archive'}
            <Archive {user_id}/>
            {/if}
        </div>
        <div>
            <div class='notice-container'>
                {#each notice_friend_ids as notice_id}
                <div>
                    <NoticeFriend on:cancel={EditFriendsNotices} notice_id={notice_id}/>
                </div>
                {/each}
                {#each notice_list_ids as notice_id}
                <div>
                    <NoticeList on:cancel={EditListsNotices} notice_id={notice_id}/>
                </div>
                {/each}
            </div>
        </div>
    </div>
</main>


<style>
    main{
        min-width: 640px;
        width: 100%; min-height: 100vh; height: fit-content;
        background-color: white;
        display: flex; flex-direction: row;
    }
    main div{
        display: flex;
        width: fit-content;
        height: fit-content;
    }
    .user-page{
        flex-direction: column;
        justify-content: start;
        align-items: center;
        width: 100%;
        min-height: 100vh;
        position: relative;
    }
    .notice-container{
        width: 100%;
        width: 330px;
        height: fit-content;
        bottom: 10px; right: 10px;
        position: absolute;
        display: flex;
        flex-direction: column;
        justify-content: end;
        align-items: center;

    }
    .nav{
        width: 100%;
        background-color: #edf2fa;
        height: 100px;
        border-bottom: 1px solid #c5c9cf;
        display: flex; flex-direction: row;
        justify-content: space-around; align-items: center;
    }
    .nav div{
        width: fit-content;
    }
    .filter-btn{
        display: flex;
        justify-content: center; align-items: center;
    }
    .filter-btn p{
        font-size: 16px;
        font-weight: 400;
    }
    .filter-btn.active p{
        font-weight: 500;
    }
    .show{
        margin-top: 10px;
        min-height: 100%;
        width: 100%;
        height: fit-content;
    }
</style>