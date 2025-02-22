<script>
import DiaryCover from "./DiaryCover.svelte";

const AddIcon = 'icons/plus_icon.svg';

let activebtn = 'all_btn';

function ShowAll(){
    activebtn = 'all_btn';
}
function ShowOwn(){
    activebtn = 'own_btn';
}
function ShowGroup(){
    activebtn = 'group_btn';
}
function ShowAdmin(){
    activebtn = 'admin_btn';
}
</script>
<style>
.diaries {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.diaries > div{
    display: flex;
    margin: 10px 0px;
    flex-direction: row;
}
.panel{
    width: 100%;
    height: 70px;
    justify-content: space-between;
    align-items: center;
}
.filter{
    display: flex;
    margin-left: 80px;
    width: 400px;
    justify-content: space-around;
}
.filter button{
    border: none;
    cursor: pointer;
    background-color: transparent;
    height: 50px;
    width: fit-content;
    transition: border-bottom -0.3s ease-in;

}
.filter button p{
    color: #616161;
    font-size: 16px;
    font-weight: 300;
}
.filter button.active{
    border-bottom: 3px solid #eceff1;
}
.filter button.active p{
    color:#424242;
    font-weight: 400;
}
.add{
    margin-right: 20px;
    width: 60px;
    height: 60px;
}
.add button{
    background-color: transparent;
    cursor: pointer;
    border: none;
    width: 60px;
    height: 60px;
}
.diaries_container{
    flex-wrap: wrap;
    justify-content: flex-start;
}
</style>

<div class='diaries'>

    <div class='panel'>
        <div class="filter">
            <button id="all_btn" class:active={activebtn === 'all_btn'} on:click={ShowAll}><p>Все</p></button>
            <button id="own_btn" class:active={activebtn === 'own_btn'} on:click={ShowOwn}><p>Личные</p></button>
            <button id="group_btn" class:active={activebtn === 'group_btn'} on:click={ShowGroup}><p>Групповые</p></button>
            <button id="admin_btn" class:active={activebtn === 'admin_btn'} on:click={ShowAdmin}><p>Управляемые</p></button>
        </div>
        <div class="add">
            <button id="add_list_btn">
                <img src={AddIcon} alt="add">
            </button>
        </div>
    </div>
    <div class='diaries_container'>
        <DiaryCover TypeCover='cover'/>
        <DiaryCover TypeCover='list'/>
        <DiaryCover />
        <DiaryCover />
        <DiaryCover />
    </div>

</div>
