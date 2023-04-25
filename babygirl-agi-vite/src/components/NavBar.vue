<script setup>
import { onMounted, ref } from 'vue'


import Conversations from './Conversations.vue'
import { store } from '../store.js'

const showMenu = ref(false)
const isEditingTitle = ref(false)

function toggleChats() {
    showMenu.value = !showMenu.value
}

</script>
<template>
    <nav class="border-gray-200 bg-gray-50 dark:bg-gray-800 bg-gray-800 dark:border-gray-700 border-gray-700">
        <div class="max-w-screen-xl flex flex-wrap items-center mx-auto p-4">
            <div class="justify-self-start">
                <a href="#" class="flex items-center">
                    <img src="/baby_rg.jpg" class="h-12 mr-3 rounded-full" alt="Flowbite Logo" />
                    <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">BabygirlAGI</span>
                </a>
            </div>
            <!-- <button data-collapse-toggle="navbar-hamburger" type="button" @click="toggleMenu"
                
                aria-controls="navbar-hamburger" aria-expanded="false">
            </button> -->
            <button data-collapse-toggle="navbar-hamburger" type="button" @click="toggleChats"
                class="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                aria-controls="navbar-hamburger" aria-expanded="false">
                <span class="sr-only">Open chats menu</span>
                <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 01-.825-.242m9.345-8.334a2.126 2.126 0 00-.476-.095 48.64 48.64 0 00-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0011.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155"></path>
                </svg>
            </button>
            <div :class="`${showMenu ? '' : 'hidden'} w-full`" id="navbar-hamburger">
                <Conversations />
            </div>
        </div>
    </nav>
</template>