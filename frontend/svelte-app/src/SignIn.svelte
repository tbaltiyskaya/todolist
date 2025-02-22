<script>
import SignInForm from "./components/SignInForm.svelte";
import SignUpForm from "./components/SignUpForm.svelte";
let ShowLogin = true;
let activebtn = 'signin'
function ShowSignUp(){
    ShowLogin = false;
    activebtn = 'signup'
}
function ShowSignIn(){
    ShowLogin = true;
    activebtn = 'signin'
}
</script>

<style>
    main{
        background-color: #607d8b;
        width: 100%;
        height: 100vh;
        display: flex;
        justify-content: space-around;
        align-items: center;
    }
    .title{
        display: flex;
        flex-direction: column;
        justify-content: center;
        border: 1px solid white;
        max-width: 420px;
        height: 150px;
    }
    .title h1{
        color: white;
        font-weight: 600;
        font-size: 56px;
    }
    .title p{
        color: white;
        font-weight: 400;
        font-size: 24px;
    }
    .signform{
        width: 380px;
        height: 400px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .wrap button{
        background-color: transparent;
        border: none;
        margin: 10px;
    }
    .wrap button p{
        color: #eceff1;
        font-size: 20px;
        font-weight: 500;
        transition: color 0.2s, transform 0.2s; 
    }
    .wrap button:hover p{
        transform: scale(0.96);
    }
    .wrap button.active p {
        color: white;
        transform: scale(1.08);
    }

</style>
<main>
    <div class='title'>
        <h1>Ежедневник.</h1>
        <p>Управление вашим списком дел, одному или в команде</p>
    </div>
    <div class='signform'>
        <div class='wrap'>
            <button id="signin_btn" class:active={activebtn === 'signin'} on:click={ShowSignIn}><p>Войти</p></button>
            <button id="signup_btn" class:active={activebtn === 'signup'} on:click={ShowSignUp}><p>Зарегистрироваться</p></button>
        </div>
        {#if ShowLogin}
            <SignInForm />
        {:else}
            <SignUpForm />
        {/if}
    </div>
</main>