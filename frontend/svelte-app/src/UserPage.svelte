<script>
import UserMenu from "./components/UserMenu.svelte";
import CommonCalendar from "./components/CommonCalendar/CommonCalendar.svelte";
import Diaries from "./components/Diaries/Diaries.svelte";
import Archive from "./components/Archives/Archive.svelte";
import Notice from "./components/notices/Notice.svelte";

let activebtn = 'calendar';

function ShowCalendar(){
    activebtn = 'calendar';
}
function ShowDiary(){
    activebtn = 'diary';
}
function ShowArchive(){
    activebtn = 'archive';
}

</script>

<style>
main{
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
}
.usermenu{
    max-width: 25%;
    height: 100%;
}
.mainpage{
    margin-left: 10px;
    min-width: 75%;
    max-height: fit-content;
    min-height: 100vh;
    background-color: white;
    display: flex;
    flex-direction: column;
    justify-content:flex-start;
    align-items: center;
}
.mainpage > div{
    width: 95%;
    margin: 20px 0px 0px;
    display: flex;

}
.notifications{
    height: 100px;
    justify-content: end;
    align-items: center;
}
.nav{
    width: 100px;
    padding-bottom: 8px;
    border-bottom: 3px solid #eceff1;
    justify-content: space-around;
    box-shadow: rgba(33, 35, 38, 0.1) 0px 10px 10px -10px;
}
.nav button{
    border: none;
    cursor: pointer;
    background-color: transparent;
    height: 50px;
    width: fit-content;
}
.nav button p{
    color: #616161;
    font-size: 18px;
    font-weight: 500;
}
.nav button.active p{
    color:#424242;
    font-weight: 600;
}
</style>

<main>
    <div class="usermenu">
        <UserMenu/>
    </div>
    <div class="mainpage">
        <div class="notifications">
            <Notice />
        </div>
        <div class="nav">
            <div>
                <button id="calendar_btn" class:active={activebtn === 'calendar'} on:click={ShowCalendar}><p>Общий календарь</p></button>
            </div>
            <div>
                <button id="diary_btn" class:active={activebtn === 'diary'} on:click={ShowDiary}><p>Ежедневники</p></button>
            </div>
            <div>
                <button id="archive_btn" class:active={activebtn === 'archive'} on:click={ShowArchive}><p>Архив дел</p></button>
            </div>
        </div>
        <div class="field">
            {#if activebtn === 'calendar'}
              <CommonCalendar />
            {:else if activebtn === 'diary'}
                 <Diaries />
            {:else if activebtn === 'archive'}
                <Archive />
            {/if}
        </div>
    </div>
</main>