<script>
    export let Type;

    import AddFriendMessage from "./AddFriendMessage.svelte";
    import JoinGroupMessage from "./JoinGroupMessage.svelte";
    import GetCaseMessage from "./GetCaseMessage.svelte";
</script>

<style>
.message{
    padding: 10px 15px;
    display: flex;
    height: 80px;
    width: fit-content;
    max-width: 240px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-radius: 8px;
    background-color: #eceff1;
    box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 1px 3px 1px;
    margin: 10px;
}

.agreement{
    display: flex;
    width: 150px;
    height: 30px;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
.agreement button{
    width: fit-content;
    height: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    border: none;
    border-radius: 4px;
}
.agreement button p{
    font-size: 12px;
}
.yes_btn{
    background-color: #ccdc39c0;
}
.no_btn{
    background-color: #e57373ac;
}

</style>

<div class='message'>
    <div class=text>
        {#if Type === 'AddFriendMessage'}
            <AddFriendMessage />
        {:else if Type === 'JoinGroupMessage'}
            <JoinGroupMessage />
        {:else if Type === 'GetCaseMessage'}
            <GetCaseMessage />
        {/if}
    </div>
    <div class="agreement">
        <button class="yes_btn"><p>Принять</p></button>
        <button class="no_btn"><p>Отклонить</p></button>
    </div>
</div>