<script>
const BellIcon = 'icons/bell_icon.svg';
let notice_stack = ' ';
let noticeCount = 12;

import Message from "./Message.svelte";
</script>
<style>
    .notice{
        display: flex;
        flex-direction: row;
    }
    .messages{
        display: flex;
        border-radius: 8px;
    }
    .bell{
        z-index: 5;
        width: 50px;
        height: 50px;
        position: relative;
        display: flex;
        justify-content: center; align-items: center;
        border-radius: 50%;
        border: none;
        background-color: transparent;
    }
    .bell img{
        width: 40px;
        height: 40px;
    }
    .notice_count{
        z-index: 10;
        position: absolute;
        top: 6px;
        right: 6px;
        border-radius: 50%;
        background-color: transparent;
    }
    .notice_count.active{
        background-color: red;
        width: 14px; height: 14px;
    }
    .bell.active img{
        animation: pulse 1.3s linear infinite alternate;
    }

    @keyframes pulse{
        0% {
        transform: rotate(-13deg);
    }
    100% {
        transform: rotate(13deg);
    }
    }
</style>

<div class='notice'>
    <div class="messages">
        <Message Type='AddFriendMessage'/>
    </div>
    <button class="bell" class:active={notice_stack =! " "}>
        <img src={BellIcon} alt="Bell">
        <div class="notice_count" class:active={noticeCount =! 0}></div>
    </button>
</div>