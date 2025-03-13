<script>
    let username = '';
    let email = '';
    let password = '';
    let copy_password = '';

    const API_URL = 'http://127.0.0.1:5000';

    const pattern = /^(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])[A-Za-z\d!@#$%^&*()_+={}\[\]:;"'<>,.?~`-]{8,}$/;

    let error = '';
    let sending = false;

    let fetched_id;

    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    function SendUserId(){
        const data = {'user_id': fetched_id};
        dispatch('SendUserId', data);
    }

    function ComparePasswords(){
        if(password == '' & copy_password == ''){
            error = '';
        }
        else if (password != copy_password){
            error = 'Пароли не совпадают';
        }
        else if(pattern.test(password)){
            error = '';
            sending = true;
        }
        else{
            error = 'Пароль должен состоять не менее чем из 8ми латинских символов, а также содержать заглавные буквы, цифры и специальные символы';
        }
    }

    async function CheckPassword() {
        console.log('ACTIVE');
        const response = await fetch(`${API_URL}/sign_up`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, email, password })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
        }
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS');
            const new_user_id = data.data;
            fetched_id = new_user_id;
            SendUserId();
        } else {
            if(data.message === 'Registration error'){
                error = 'Произошла ошибка регистрации';
            }
            console.log('ERROR');
        }
    }
</script>

<div class='form-block'>
    <form on:submit|preventDefault={CheckPassword()}>
        <div class='label'><p>Придумайте имя</p></div>
        <div><input type="text" bind:value={username} required autocomplete="username" name="name"></div>
        
        <div class='label'><p>Укажите почту</p></div>
        <div><input type="email" bind:value={email} required autocomplete="email" name="email"></div>

        <div class='label'><p>Придумайте пароль</p></div>
        <div><input type="password" bind:value={password} on:input={ComparePasswords()} required autocomplete="current-password" name="password" ></div>
        
        <div class='label'><p>Повторите пароль</p></div>
        <div><input type="password" bind:value={copy_password} on:input={ComparePasswords()} required autocomplete="current-password" name="copypassword"></div>

        <div class='warning'>
            <p>{error}</p>
        </div>

        <div>
            <button class="submit" type="submit" disabled={!sending}><p>Зарегистрироваться</p></button>
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