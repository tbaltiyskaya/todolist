<script>
export let Username;
export let Email;

const SettingsIcon = 'icons/settings_icon.svg';
</script>
<style>
.usermenu{
    width: 100%;
    height: 100vh;
    background-color: #eceff1;
    box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
    display: flex;
    flex-direction: column;
    justify-content:flex-start;
    align-items: flex-start;
}
.info {  
    padding: 30px 10px;
    display: grid;
    grid-template-columns: 60px 220px 60px;
    grid-template-rows: 35px 25px;
    gap: 0px 5px;
    grid-auto-flow: row;
    grid-template-areas:
    "icon username settings"
    "icon email settings";
}
.info div{
    border: 1px solid black;
    display: flex;
    justify-content: center;
    align-items: center;
}

.icon { 
    grid-area: icon;
    border-radius: 50%;
    overflow: hidden;
}

.username {
    grid-area: username;
}
.username p{
    font-size: 16px;
    font-weight: 500;
}
.email { grid-area: email; }
.email p{
    font-size: 14px;
    font-weight: 200;
}
.settings {
    grid-area: settings;
 }
.settings img{
    width: 50%;
}

</style>

<div class="usermenu">
    <div class="info">
        <div class="icon">

        </div>
        <div class="username">
            <p>{Username}</p>
        </div>
        <div class="email">
            <p>{Email}</p>
        </div>
        <div class="settings">
            <img src={SettingsIcon} alt="Settings">
        </div>
    </div>

</div>
