<script setup>
import { onMounted, ref, computed } from 'vue'
import { initFlowbite } from 'flowbite'

import NavBar from './components/NavBar.vue';
import Chat from './components/Chat.vue';
import { store } from './store'

// initialize components based on data attribute selectors
onMounted(() => {
    initFlowbite();
})

</script>

<template>
    <div class="bg-gradient-to-br from-gray-900 to-slate-900/[.9] h-screen w-screen">
        <NavBar />
        <router-view class="pt-20"></router-view>
    </div>
</template>

<style scoped>
.logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
}

.logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
    filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
