<script>
    export let icon;
    export let onClick;
    export let disabled;

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
        width: 40px;
        height: 40px;
    }
    .icon-btn img{
        width: 36px;
        transition: all 0.3s linear;
    }
    .icon-btn img:hover{
        opacity: 0.7;
    }
    .icon-btn img:active{
        width: 30px;
    }
    .icon-btn:disabled{
        opacity: 0.5;
        cursor: not-allowed;
    }
</style>

<div>
    <button class="icon-btn"
    on:click={handleClick}
    disabled={disabled}>
        <img src={icon} alt="icon"> 
    </button>
</div>
