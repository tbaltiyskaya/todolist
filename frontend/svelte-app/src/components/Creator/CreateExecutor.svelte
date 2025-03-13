<script>
    import User from "../Users/User.svelte";
    export let executor_id;
    export let executor_name;
</script>

<div class="executor"><p>Исполнитель: {executor_name}</p></div>

<style>
    .executor{
        border: 1px solid yellowgreen;
        width: fit-content;
        height: fit-content;
    }
</style>