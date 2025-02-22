<script>

import ToDoItem from "../Item/ToDoItem.svelte";

</script>
<style>
    .archive{
        width: 100%;
        height: fit-content;
        display: flex;
        justify-content: center;
    }
    .item-container{
        width: 90%;
        height: fit-content;
        border: 1px solid black;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>

<div class='archive'>
    <div class="item-container">
        <ToDoItem />
        <ToDoItem />
        <ToDoItem />
    </div>
</div>