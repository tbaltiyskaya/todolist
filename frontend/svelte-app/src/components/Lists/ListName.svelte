<script>
    export let list_id;
    let list_name;
    let loading = false;
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    const API_URL = 'http://127.0.0.1:5000';



    function SendListId(){
        const data = {'list_id': list_id};
        dispatch('SendListId', data);
    }

    async function ShowListName() {
        const response = await fetch(`${API_URL}/get_list_name`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ list_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка: ', errorData);
            console.log('Нет соединения')
        }
        console.log('SENT');
        const data = await response.json();
        if (data.status === 'success') {
            console.log('SUCCESS LISTS OWN');
            const listname = data.data;
            list_name = listname;
            loading = true;

        } 
        else {
            console.log('ERROR');
        }
    }

    ShowListName();
</script>

{#if loading}
    <div class="list">
        <button on:dblclick={() => SendListId()}><p>{list_name}</p></button>
    </div>
{/if}

<style>
    .list{
        width: 200px;
        height: fit-content;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .list button{
        width: 100%;
        height: 30px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>