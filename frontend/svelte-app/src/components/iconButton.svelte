<script>
    export let icon;
    export let onClick;
    export let disabled = false;

    function handleClick() {
        if (!disabled && onClick) {
            onClick();
        }
    }

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
    <button class="icon-btn"
    on:click={handleClick}
    disabled={disabled}>
        <img src={icon} alt="icon"> 
    </button>
</div>
