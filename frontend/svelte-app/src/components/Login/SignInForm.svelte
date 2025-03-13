<script>
    let username = '';
    let password = '';

    const API_URL = 'http://127.0.0.1:5000';

    let error = '';
    let enter = false;

    let fetched_id;

    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    function SendUserId(){
        const data = {'user_id': fetched_id};
        dispatch('SendUserId', data);
    }


    async function CheckPassword() {
        const response = await fetch(`${API_URL}/sign_in`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS');
            error = 'Успешно вошли';
            enter = true;
            const user_id = data.data;
            fetched_id = user_id;
            SendUserId();

        } else if (data.status === 'error'){
            console.log('ERROR');
            error = 'Неверное имя или пароль';
        }
    }
</script>

<div class='form-block'>
    <form on:submit|preventDefault={CheckPassword()}>
        <div class='label'><p>Имя пользователя</p></div>
        <div><input type="text" bind:value={username} required autocomplete="username"></div>
        
        <div class='label'><p>Пароль</p></div>
        <div><input type="password" bind:value={password} required autocomplete="current-password"></div>
        <div class='warning'>
            <p>{error}</p>
        </div>
        <div>
            <button class="submit" type="submit"><p>Войти</p></button>
        </div>
    </form>
</div>

<style>
    .form-block{
        width: 400px;height: fit-content;
        background-color: #edf2fa; 
        border-radius: 8px;
        padding: 5px;
        box-shadow: rgba(0, 0, 0, 0.19) 0px 10px 20px, rgba(0, 0, 0, 0.23) 0px 6px 6px;
    }
    form{
        width: 100%; height: fit-content;
        display: flex; 
        flex-direction: column;
        justify-content: start; align-items: center;
    }
    .form-block p{
        color: black; font-size: 14px;
    }
    form div{
        margin: 3px;
        display: flex;
        justify-content: center; align-items: center;
    }
    form input{
        width: 270px;
        border-radius: 4px;
    }
    .label{
        text-align: left;
        height: 25px;
    }
    .submit{
        display: flex; justify-content: center; align-items: center;
        width: fit-content; min-width: 120px; height: 45px;
        padding: 10px; margin: 6px;
        background-color: #abc4ff; border-radius: 4px;
        transition: all 0.3s 0s;
    }
    .submit p{
        font-size: 16px;
        color: white;
    }
    .submit:hover{
        background-color: #c1d3fe;
    }
    .submit:active{
        transform: scale(95%);
    }
    .submit:disabled{
        cursor: none;
        background-color: #d7e3fc;
    }
    .submit:active{
        transform: scale(95%);
    }
    .warning{
        width: 270px;
    }
    .warning p{
        text-align: center;
        font-size: 12px;
        font-weight: 300;
        color: red;
    }
</style>