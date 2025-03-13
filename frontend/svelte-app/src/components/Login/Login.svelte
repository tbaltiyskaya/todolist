<script>
    let Form = true;
    import UserPage from "../Users/UserPage.svelte";
    import SignInForm from "./SignInForm.svelte";
    import SignUpForm from "./SignUpForm.svelte";

    let user_id;
    let show_userpage = false;

    function SwitchForm(form){
        Form = (form === 'signin');
    }

    function GetUserPage(event){
        user_id = event.detail.user_id;
        show_userpage = true;
    }
</script>


{#if show_userpage}
<UserPage user_id={user_id}/>
{:else}
<main>
    <div class='title'>
        <h1>ToDoList</h1>
        <p>tasks for everyone</p>
    </div>
    <div class='login-form'>
        <div class='switch'>
            <button class='SignIn' on:click={() => SwitchForm('signin')}>
                <p style="font-size: {Form ? '18px' : '16px'};">Войти</p>
            </button>
            <button class='SignUp' on:click={() => SwitchForm('signup')}>
                <p style="font-size: {Form ? '16px' : '18px'};">Зарегистрироваться</p>
            </button>
        </div>
        <div class='form-block'>
            {#if Form}
	            <p><SignInForm on:SendUserId={GetUserPage}/></p>
            {:else}
	            <p><SignUpForm on:SendUserId={GetUserPage}/></p>
            {/if}
        </div>
    </div>
</main>
{/if}


<style>
    main{
        background: #abc4ff;
        background: linear-gradient(90deg, #abc4ff 30%, #d7e3fc 100%);
        width: 100vw;height: 100vh;
        display: flex;
        flex-direction: row; justify-content: space-around; align-items: center;
    }
    main p{
        color: white;
        font-size: 16px;
        font-weight: 400;
    }
    .title{
        width: 400px;
        display: flex; flex-direction: row;
        justify-content: center; align-items: center;
    }
    .title h1{
        color: white;
        font-size: 70px;
        font-weight: 600;
        margin: 5px;
    }
    .login-form{
        width: 400px;height: 400px;
        display: flex; flex-direction: column;
        align-items: center; justify-content: start;
    }
    .switch{
        width: 400px;height: 60px;
        display: flex; flex-direction: row;
        justify-content: space-between;
    }
    .switch button{
        height: 60px;
    }
    .switch .SignIn{width: 160px;}
    .switch .SignUp{width: 230px;}

    .form-block{
        display: flex;
        justify-content: center;
        align-items: start;
    }


</style>