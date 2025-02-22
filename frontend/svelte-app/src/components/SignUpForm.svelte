<script>
    let email = '';
    let username = '';
    let password = '';
    let replaced_password = '';
    function SignUpCheck(){}
</script>

<style>
    .formcontainer{
        background-color: #eceff1;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
        width: 100%;
        padding: 20px;
        border-radius: 8px;
    }
    form {
        display: flex;
        flex-direction: column;
        align-items: center;
        min-width: 300px;
    }
    input{
        width: 90%;
        margin: 5px;
    }
    button{
        min-width: 120px;
        width: fit-content;
        height: 50px;
        margin: 15px;
        padding: 10px;
        background-color: #78909c;
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: color 0.2s, transform 0.2s; 
    }
    button:hover{
        background-color: #b0bec5;
    }
    button:active{
        transform: scale(0.94);
    }
    button p{
        font-size: 18px;
        font-weight: 400;
        color: white;
    }
</style>

<div class='formcontainer'>
    <form on:submit={SignUpCheck}>
        <input type="text" placeholder="Имя пользователя" bind:value={username} required />
        <input type="email" placeholder="Email" bind:value={email} required />
        <input type="password" placeholder="Придумайте пароль" bind:value={password} required />
        <input type="password" placeholder="Повторите пароль" bind:value={replaced_password} required />
        <button type="submit"><p>Зарегистрироваться</p></button>
    </form>
</div>
