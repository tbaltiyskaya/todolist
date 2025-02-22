<script>
    export let icon;
    export let onClick;
</script>
<style>
    .icon-btn{
        background-color: transparent;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 26px;
        height: 26px;
    }
    .icon-btn img{
        width: 24px;
    }
    .icon-btn img:hover{
        opacity: 0.7;
    }
    .icon-btn img:active{
        width: 22px;
    }
</style>

<div>
    <button class="icon-btn" on:click|preventDefault={onClick}>
        <img src={icon} alt="icon"> 
    </button>
</div>
