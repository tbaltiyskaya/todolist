<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    const API_URL = 'http://127.0.0.1:5000';
    
    export let list_id;
    export let list_name;

    let errorMessage = '';
    let canSent = false;

    let tempName = list_name;
    let nameDiv;


    function CheckLength(){
        if (tempName.length > 40){
            errorMessage = 'Длина названия не должна превышать 40 символов';
            canSent = false;
        }
        else if(tempName.length == 0){
            errorMessage = 'Укажите название листа';
            canSent = false;
        }
        else{
            errorMessage = '';
            canSent = true;
        }
    }

    function handleInput(event) {
        tempName = event.target.innerText;;
        CheckLength();
    }
    
    $: {
        if(nameDiv){
            if (nameDiv.innerText !== tempName){
                nameDiv.innerText = tempName;
            }
        }
    }

    function Cancel(){
        dispatch('cancel');
    }

    async function RenameList() {
        const response = await fetch(`${API_URL}/rename_list`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ list_id, tempName })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            console.log('Нет соединения')
        }
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS EDIT LIST');
            Cancel();
        } else {
            console.log('ERROR');
        }
    }


</script>

<div class="editor">
    <div class='block-header'><p>Переименовать лист</p></div>
    <div class="data">
        <div class="header"><p>Название листа</p></div>

        <div bind:this={nameDiv} class="name" contenteditable="true"
            on:input={handleInput} 
            placeholder="Введите имя">
        </div>

        <div class='warning'>
            <p>{errorMessage}</p>
        </div>
    </div>
    <div class="buttons">
        <button class="cancel" on:click={Cancel}><p>Отмена</p></button>
        <button class="save" disabled={!canSent} on:click|preventDefault={() => RenameList()}><p>Сохранить</p></button>
    </div>
</div>


<style>
    .editor{
        position: absolute;
        top:10%; left: 30%;
        z-index: 10;
        width: 400px;height: 200px;
        padding: 10px; border-radius: 8px;
        background-color: white;
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
        display: flex; flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
    .editor > div{
        width: 90%;
    }
    .block-header{
        display: flex; justify-content: center; align-items: center;
        width: fit-content; height: 30px;
    }
    .block-header p{
        font-size: 16px;
        font-weight: 600;
    }
    .data{
        height: 200px;
        display: flex; flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
    .data > div{
        width: 100%;
    }
    .name{
        min-height: 25px;
        display: flex; align-items: center; flex-wrap: wrap;
        padding-left: 5px;
        font-size: 16px;
        border-bottom: 2px solid black;
    }
    .buttons{
        height: fit-content;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }
    .buttons button{
        background-color: #abc4ff;
        border-radius: 8px;
        width: 90px;
        height: 30px;
        transition: all 0.2s ease;
    }
    .buttons button:disabled{
        cursor: not-allowed;
        background-color: #edf2fa;
    }
    .buttons button:hover{
        background-color: #c1d3fe;
    }
    .buttons button:active{
        transform: scale(97%);
    }
    .buttons button p{
        font-size: 12px;
        font-weight: 400;
    }
    .warning{
        height: 30px;
        display: flex; justify-content: center; align-items: center;
    }
    .warning p{
        text-align: center;
        font-size: 12px;
        font-weight: 300;
        color: red;
    }
</style>