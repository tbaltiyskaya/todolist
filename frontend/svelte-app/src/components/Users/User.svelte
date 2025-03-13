<script>
    export let user_id;
    import { onMount } from 'svelte';
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    const UserIcon = '/icons/user_icon.svg';
    const API_URL = 'http://127.0.0.1:5000';


    let username = '';
    let email = '';

    async function ShowUser() {
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
            console.log('SUCCESS');
            const { username: fetchedUsername, email: fetchedEmail } = data.data;
            username = fetchedUsername;
            email = fetchedEmail;
            SendUsername();
        } else {
            console.log('ERROR');
        }
    }

    function SendUsername(){
        const data = {'username': username};
        dispatch('SendUsername', data);
    }

    onMount(() => {
        ShowUser();
    });
</script>


<div class='user'>
    <div class="icon">
        <img src={UserIcon} alt="">
    </div>
    <div class="username"><p class="p-username">{username}</p></div>
    <div class="email"><p class="p-useremail">{email}</p></div>
</div>

<style>
    .user {
        width: 220px;height: 40px;
        padding: 5px;
        display: grid; 
        grid-template-columns: 40px 170px; 
        grid-template-rows: 20px 20px; 
        gap: 0px 5px; 
        grid-template-areas: 
        "icon username"
        "icon email";  
    }
    .user div{
        display: flex; justify-content: center; align-items: center;
    }
    .icon {
        width: 40px;height: 40px;
        border-radius: 50%; overflow: hidden;
        border: 1px solid black;
        grid-area: icon;
    }
    .icon img{
        width: 100%;
    }
    .username { grid-area: username; }
    .email { grid-area: email; }

</style>