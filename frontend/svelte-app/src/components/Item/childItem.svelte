<script>
    let text = 'банан';
    let isStrikethrough = false;

    function toggleStrikethrough() {
        isStrikethrough = !isStrikethrough;
    }
</script>

<style>
    li {
        list-style-type: none;
        margin-bottom: 15px;
    }
    li a {
        font-size: 16px;
        font-weight: 400;
        text-decoration: none;
        cursor: pointer;
        color: inherit;
        display: inline-block;
    }
    li a.strikethrough {
        text-decoration: line-through; /* Зачеркивание текста */
    }
</style>

<li>
    <div>
        <a 
            href="none"
            class={isStrikethrough ? 'strikethrough' : ''} 
            on:click|preventDefault={toggleStrikethrough} 
            on:keydown={event => {
                if (event.key === 'Enter' || event.key === ' ') {
                    toggleStrikethrough();
                }
            }} 
            tabindex="0">
            {text}
        </a>
    </div>
</li>