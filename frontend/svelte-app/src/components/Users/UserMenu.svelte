<script>
    import IconButton from "../Buttons/iconButton.svelte";
    import LargeButton from "../Buttons/LargeButton.svelte";
    import Friends from "./Friends.svelte";
    import User from "./User.svelte";
    import UserFriend from "./UserFriend.svelte";
    const SettingsIcon = '/icons/settings_icon.svg';
    const MenuIcon = '/icons/menu_icon.svg';
    const SearchIcon = '/icons/search_icon.svg';
    const CloseIcon = '/icons/close_icon.svg';
    const API_URL = 'http://127.0.0.1:5000';

    export let user_id;

    let find_username = '';
    let find_username_div;
    let finded_user_id = -1;
    let add = true;

    let show_finded_user = false;

    let hide = false;

    function handleInput(event) {
        find_username = event.target.innerText;
    }

    async function FindFriend() {
        const response = await fetch(`${API_URL}/find_friend`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id, find_username })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
        }
        const data = await response.json();
        if (data.status === 'success') {
            const { 
                user_id: fetchedId,
                add: fetchedAdd,
            } = data.data;
            finded_user_id = fetchedId;
            add = fetchedAdd;
            console.log('new data = ', finded_user_id, add);
            show_finded_user = true;
        } else {
            console.log('ERROR');
        }
    }

    function RefreshSearch(){
        show_finded_user = false;
        finded_user_id = -1;
        if (find_username_div){
            find_username_div.innerText = '';
            find_username = '';
        }
    }

    function HideMenu(){
        hide = !hide;
    }

</script>


<div class="menu">
    <div class='user-menu {hide ? 'hided' : ''}'>
        <div class='user'>
            <div>
                <User {user_id}/>
            </div>
            <div class='settings'>
                <LargeButton icon={SettingsIcon} />
            </div>
        </div>
        <div class='find-friends'>
            <div><p>Найти друзей</p></div>
            <div class="find-block">
                <div class="finder">
                    <div bind:this={find_username_div} class="username" contenteditable="true"
                        on:input={handleInput} 
                        placeholder="Введите имя">
                    </div>
                    <div><IconButton icon={SearchIcon} onClick={FindFriend}/></div>
                    <div><IconButton icon={CloseIcon} onClick={RefreshSearch}/></div>
                </div>
                <div class="result">
                    {#if finded_user_id == -1}
                    <div>
                        <p class="p-light">Найдите пользователя, указав полное имя.</p>
                    </div>
                    {/if}
                    {#if show_finded_user}
                        {#if finded_user_id == 0}
                            <div>
                                <p class="p-light">Пользователь с данным именем не найден.</p>
                            </div>
                        {:else if finded_user_id > 0 && add}
                            <div>
                                <UserFriend watcher_id={user_id} user_id={finded_user_id} subject_id=0 operation='friend_create'/>
                            </div>
                        {:else if finded_user_id > 0 && !add}
                            <div>
                                <UserFriend watcher_id={user_id} user_id={finded_user_id} subject_id=0 operation='friend_delete'/>
                            </div>
                        {/if}
                    {/if}
                </div>
            </div>
        </div>
        <div class='friends'>
            <Friends watcher_id={user_id} subject_id=0 operation='friend_delete'/>
        </div>
    </div>
    <div class="hide">
        {#if hide}
            <LargeButton icon={MenuIcon} onClick={HideMenu}/>
        {:else}
            <LargeButton icon={MenuIcon} onClick={HideMenu}/>
        {/if}
    </div>
</div>


<style>
    .menu{
        width: fit-content;
        height: fit-content;
        display: flex;
        flex-direction: row;
        justify-content: start; align-items: start;
        background-color: white; border-right: 1px solid #c5c9cf;
    }
    .hide{
        width: fit-content;min-height: 100vh; padding: 15px 5px 0 0;
        display: flex; flex-direction: column;
        justify-content: start; align-items: center;
    }
    .user-menu{
        width: 360px; min-height: 100vh; height: fit-content;
        display: flex; flex-direction: column;
        justify-content: start;align-items: center;
        z-index: 5;
    }
    .user-menu.hided{
        display: none;
    }
    .user-menu > div{
        margin: 10px 0px;
    }
    .user{
        display: flex;flex-direction: row;
        width: fit-content; height: fit-content; padding: 4px;
        justify-content: center; align-items: center;
        border: 1px solid #c5c9cf;border-radius: 8px;
    }
    .friends{
        width: fit-content; height: fit-content;
        display: flex; flex-direction: column;
        justify-content: start;
        align-items: center;
    }
    .find-friends{
        width: 300px; height: 196px;
        display: flex; flex-direction: column;
        justify-content: start; align-items: center;
    }
    .find-friends > div{
        margin: 10px;
    }
    .find-block{
        width: 100%; height: fit-content;
        padding: 4px;
        display: flex; flex-direction: column;
        justify-content: center; align-items: center;
        background-color: #edf2fa;
        border: 1px solid #c5c9cf;
        border-radius: 8px;
    }
    .finder{
        width: 100%; height: fit-content;
        display: flex; flex-direction: row;
        justify-content: space-around; align-items: center;
        margin: 10px 0px;
    }
    .finder .username{
        background-color: white;
        height: 26px;
        width: 230px;
        padding: 0px 5px;
        display: flex; justify-content: start; align-items: center;
        border: 1px solid #c5c9cf;
        border-radius: 8px;
    }
    .result{
        display: flex; justify-content: center; align-items: center;
    }
    .result div{
        display: flex; justify-content: center; align-items: center;
    }
</style>