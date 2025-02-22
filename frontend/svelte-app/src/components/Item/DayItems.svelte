<script>
    export let date;

    function ConvertDate(date){
        return date.toLocaleDateString(); 
    }
</script>
<style>
.items-container{
    display: flex;
    flex-direction: column;
    justify-content:flex-start;
    align-items: center;
    border: 1px solid black;
    width: 600px; height: fit-content;
}
</style>

<div class="items-container">
    <p>{ConvertDate(date)}</p>
</div>