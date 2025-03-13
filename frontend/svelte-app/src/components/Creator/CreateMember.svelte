<script>
    export let author_id;
    export let member_id;
    export let list_id;
    export let member_name;
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    const API_URL = 'http://127.0.0.1:5000';

    function Cancel(){
        dispatch('cancel');
    }

    async function CreateMember() {
        const response = await fetch(`${API_URL}/req_add_member`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ author_id, member_id, list_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            console.log('Нет соединения')
        }
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            Cancel();
        } else {
            console.log('ERROR');
        }
    }
</script>

<div class="creator">
    <div class='block-header'><p>Приглашение</p></div>
        <div class="header"><p>Пригласить пользователя {member_name} в лист?</p></div>
    <div class="buttons">
        <button class="cancel" on:click={Cancel}><p>Отмена</p></button>
        <button class="save" on:click|preventDefault={() => CreateMember()}><p>Пригласить</p></button>
    </div>
</div>

<style>
.creator{
    position: absolute;
    top:10%; left: 0%;
    z-index: 15;
    width: 400px;height: 100px;
    padding: 10px; border-radius: 8px;
    background-color: white;
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    display: flex; flex-direction: column;
    justify-content: space-between;
    align-items: center;
}
.creator > div{
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

</style>