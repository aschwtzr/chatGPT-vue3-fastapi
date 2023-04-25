<script setup>
import { store } from '../store'
import { postConversationMessage, createNewConversation } from '../api/babygirl-api'
import { onMounted, ref, computed } from 'vue'

const currentMessage = ref('')

async function newConversation() {
    const res = await createNewConversation(currentMessage.value)
    if (!res.error) {
        store.currConversationId = `${res.id}`
        store.conversations.push(res)
        // conversations.value[res.conversationId] = {
        //     messages: [currentMessage.value],
        //     responses: [res.response]
        // }
        currentMessage.value = ''
        console.log(res)
    } else {
        console.log(res.error)
    }
}

async function updateConversation() {
    console.log(`updating ${store.currConversationId}`)
    const res = await postConversationMessage(store.currConversationId, currentMessage.value)
    if (!res.error) {
        store.updateconversationMessages(res)
        currentMessage.value = ''
        console.log(res)
    } else {
        console.log(res.error)
    }
}


const currentConversation = computed(() => {
    console.log(store.currConversationId)
    if (store.currConversationId.length) {
        console.log(store.conversations[store.currConversationId])
        return store.conversations[store.currConversationId]
    }

    return {}
})
</script>
<template>
    <div class="">
        <div v-if="store.currConversationId.length && store.conversationMessages.length">
            <h3 class="mb-2 text-center text-xl font-bold tracking-tight white:text-gray-900 dark:text-white">{{
                store.currentConversation().title }}</h3>
            <ul class="max-w-md md:max-w-full divide-y divide-gray-200 dark:divide-gray-700">
                <li class="pb-3 sm:pb-4" v-for="(chatMessage, index) in store.conversationMessages" :key="index">
                    <div class="flex flex-col justify-center items-start">
                        <div>
                            msg:
                            {{ chatMessage.message }}
                        </div>
                        <div>
                            rsp:
                            {{ chatMessage.response }}
                        </div>
                    </div>
                </li>
            </ul>
        </div>
        <form>
            <label for="default-search"
                class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
            <div class="relative">
                <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                    <svg aria-hidden="true" class="w-5 h-5 text-gray-500 dark:text-gray-400" fill="none"
                        stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                    </svg>
                </div>
                <input type="search" id="default-search"
                    class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    v-model="currentMessage" placeholder="Enter your message to the brain here" required>
                <button type="submit" @click.prevent="updateConversation" v-if="store.currConversationId.length"
                    class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">GO</button>
                <button type="submit" @click.prevent="newConversation" v-else
                    class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">GO</button>
            </div>
        </form>
    </div>
</template>