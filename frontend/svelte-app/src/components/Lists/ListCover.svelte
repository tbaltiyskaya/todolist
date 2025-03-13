<script>
    import { onMount } from 'svelte';
    import { createEventDispatcher } from 'svelte';
    import IconButton from "../Buttons/iconButton.svelte";
    import EditList from '../Editor/EditList.svelte';
    import DeleteList from '../Detelor/DeleteList.svelte';
    const EditIcon = '/icons/edit_icon.svg';
    const DeleteIcon = '/icons/delete_icon.svg';
    const GroupIcon = '/icons/group_icon.svg';
    const OwnIcon = '/icons/lock_icon.svg';
    const API_URL = 'http://127.0.0.1:5000';
    const dispatch = createEventDispatcher();

    export let list_id;
    export let user_id;

    let loading = false;

    let rename_list = false;
    let delete_list = false;

    let list_name;
    let author;
    let datetype;
    let grouptype;


    async function ListCover() {
        const response = await fetch(`${API_URL}/show_list_cover`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ list_id })
        });
        if (!response.ok) {
            const errorData = await response.json();
            console.log('Ошибка обложки листа: ', errorData);
            return;
        }
        const data = await response.json();
        if (data.status === 'success') {
            const { 
                list_name: fetchedListname,
                author: fetchedAuthor,
                datetype: fetchedDatetype, 
                grouptype: fetchedGrouptype
            } = data.data;

            list_name = fetchedListname;
            author = fetchedAuthor;
            datetype = fetchedDatetype;
            grouptype = fetchedGrouptype;
            loading = true;
        } else {
            console.log('ERROR');
        }
    }
    onMount(() => {
       ListCover();
    });

    function ListSelect(){
        const data = {
            'list_id': list_id, 
            'list_name': list_name, 
            'list_author': author,
            'list_datetype': datetype,
            'list_grouptype': grouptype
         };
        dispatch('ListSelect', data);
    }

    function ListEdit(){
        rename_list = true;
    }

    function CancelListEdit(){
        rename_list = false;
    }

    function ListDelete(){
        delete_list = true;
    }
    function CancelListDelete(){
        delete_list = false;
    }
</script>

{#if loading}

    <div class="list-cover {datetype ? 'dated' : ''}">
        {#if rename_list}
        <EditList {list_id} {list_name} on:cancel={CancelListEdit}/>
        {/if}
        {#if delete_list}
        <DeleteList {list_id} {user_id} {list_name} on:cancel={CancelListDelete}/>
        {/if}
        <button class='list-select' on:dblclick={() => ListSelect()}>
        <div class="name"><p>{list_name}</p></div>
        <div class="type">
            {#if grouptype}
                <img src={GroupIcon} alt="Group">
            {:else}
                <img src={OwnIcon} alt="Own">
            {/if}
        </div>
        </button>
        <div class="panel">
            <IconButton icon={EditIcon} onClick={() => ListEdit()}/>
            <IconButton icon={DeleteIcon} onClick={() => ListDelete()}/>
        </div>  
    </div>
{/if}

<style>
    .list-select{
        width: 100%;
        height: 150px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
    .list-select > div{
        margin: 10px;
    }
    .list-cover{
        width: 150px;
        height: 200px;
        margin: 30px;
        background-color: #faf7ef;
        display: flex;flex-direction: column;
        justify-content:space-between;align-items: center;
        box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px, rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;
        border-radius: 2px;
    }
    .type{
        width: 20px;
        height: 20px;
        display: flex; justify-content: center; align-items: center;
    }
    .type img{
        width: 100%;
    }
    .list-cover.dated{
        width: 150px;
        height: 200px;
        margin: 30px;
        background-color: #c1d3fe;
        display: flex;flex-direction: column;
        justify-content:space-between;align-items: center;
        box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
        border-radius: 2px 10px 10px 2px;
    }
    .name{
        margin-top: 20px;
        padding: 5px;
        width: 80%;
        height: fit-content;
        border: 1px solid #c5c9cf;
        border-radius: 8px;
        background-color: white;
    }
    .name p{
        font-size: 12px;
        font-weight: 500;
        text-align: center;
    }
    .panel{
        z-index: 3;
        width: 80%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
</style>