<script setup>
import { onMounted, ref } from 'vue'
import { 
    getAllConversations
} from '../api/babygirl-api'
import ConversationButton from './ConversationButton.vue'
import { store } from '../store.js'

const showMenu = ref(false)
const isEditingTitle = ref(false)
onMounted(() => {
    getAllConversations().then((res) => {
        console.log(res)
        store.conversations = res
    })
})

function toggleMenu() {
    showMenu.value = !showMenu.value
}

</script>
<template>
    <nav class="border-gray-200 bg-gray-50 dark:bg-gray-800 bg-gray-800 dark:border-gray-700 border-gray-700">
        <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
            <a href="#" class="flex items-center">
                <img src="https://flowbite.com/docs/images/logo.svg" class="h-8 mr-3" alt="Flowbite Logo" />
                <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Flowbite</span>
            </a>
            <button data-collapse-toggle="navbar-hamburger" type="button" @click="toggleMenu"
                class="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                aria-controls="navbar-hamburger" aria-expanded="false">
                <span class="sr-only">Open main menu</span>
                <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd"
                        d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                        clip-rule="evenodd"></path>
                </svg>
            </button>
            <div :class="`${showMenu ? '' : 'hidden'} w-full`" id="navbar-hamburger">
                <div class="w-full">
                    <ConversationButton :conversationId="'new'" :title="'Untitled Conversation'" />
                </div>
                <h5 id="drawer-left-label"
                    class="inline-flex items-center mb-4 text-base font-semibold text-gray-500 dark:text-gray-400"><svg
                        class="w-5 h-5 mr-2" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
                            clip-rule="evenodd"></path>
                    </svg>Previous Conversations</h5>
                <ul class="flex flex-col font-medium mt-4 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
                    <Suspense>
                        <template #fallback>
                            <div>loading yo..</div>
                        </template>
                        <template #default>
                            <ul class="space-y-2 font-medium">
                                <li v-for="conversation in store.conversations" :key="conversation.id">
                                    <ConversationButton :conversationId="conversation.id" :title="conversation.title" />
                                </li>
                            </ul>
                        </template>
                    </Suspense>
                </ul>
            </div>
        </div>
    </nav>
</template>