<script>
    import { Router, Route, Link } from 'svelte-routing';
    import SignIn from './SignIn.svelte';
	import UserPage from './UserPage.svelte'; 
</script>
<style>
</style>

<main>
    <Router>
        <nav>
            <Link to="/signin">О нас</Link>
            <Link to="/userpage"> пользователь</Link>
        </nav>
        <Route path="/signin" component={SignIn} />
        <Route path="/userpage" component={UserPage}/>
    </Router>
</main>
