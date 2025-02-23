<script>
    
export let UserID;
import { createEventDispatcher } from 'svelte';
const dispatch = createEventDispatcher();

    function handleClick() {
        dispatch('click');
    }
let Username = UserID;
let Email = UserID;
</script>
<style>
.select-user-btn{
    background-color: transparent;
    width: fit-content;
    height: fit-content;
    display: flex;
    justify-content: center;
    align-items: center;
}
.select-user-btn:hover .user{
    box-shadow: rgba(3, 102, 214, 0.3) 0px 0px 0px 3px;
}
.select-user-btn:active .user{
    background-color: aliceblue;
}
.user{
    background-color: white;
    border-radius: 8px;
    box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
    width: 180px;
    height: 35px;
    padding: 10px;
    margin: 2px;
    display: grid;
    grid-template-columns: 30px 150px;
    grid-template-rows: 20px 15px;
    gap: 0px 5px;
    grid-auto-flow: row;
    grid-template-areas:
    "icon username"
    "icon email";
}
.user div{
    display: flex;
    justify-content: center;
    align-items: center;
}
.icon { 
    grid-area: icon;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    border: 1px solid gray;
    overflow: hidden;
}
.username {
    grid-area: username;
}
.username p{
    font-size: 10px;
    font-weight: 500;
}
.email { grid-area: email; }
.email p{
    font-size: 8px;
    font-weight: 200;
}
</style>
<button class='select-user-btn' on:click={handleClick}>
    <div class='user'>
        <div class="icon">
        </div>
        <div class="username">
            <p>{Username}</p>
        </div>
        <div class="email">
            <p>{Email}</p>
        </div>
    </div>
</button>
