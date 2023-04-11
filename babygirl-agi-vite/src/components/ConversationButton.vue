<script setup>
import { ref } from 'vue'
import {
    getConversationMessages,
    updateConversationTitle,
    createNewNamedConversation
} from '../api/babygirl-api'
import { store } from '../store.js'
const props = defineProps(['conversationId', 'title'])

const newConversationTitle = ref('')
const isEditingTitle = ref(false)

function setConversation(id) {
    store.setCurrentConversation(id)
    getConversationMessages(id).then((res) => {
        console.log(res)
        store.conversationMessages = res
    })
}

function createNamedConversation() {
    createNewNamedConversation(newConversationTitle.value).then((res) => {
        console.log(res)
        const updated = [...store.conversations]
        updated.push(res)
        store.conversations = [...updated]
        // store.conversations[res.conversationId] = {
        //     title: newConversationTitle.value,
        //     chat_messages: []
        // }
        store.setCurrentConversation(res.id)
        newConversationTitle.value = ''
        isEditingTitle.value = false
    })
}

function updateTitle(conversationId) {
    updateConversationTitle(conversationId, newConversationTitle.value).then((res) => {
        console.log(res)
        store.updateConversationTitle(newConversationTitle.value)
    })
    isEditingTitle.value = false
}

function toggleEditTitle() {
    newConversationTitle.value = store.currentConversation().title
    isEditingTitle.value = !isEditingTitle.value
}

function deleteConversation(id) {
    console.log(`deleting ${id}`)
}

</script>
<template>
    <span v-if="conversationId === 'new'">
        <input type="text" 
            class="block w-8/12 p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            v-model="newConversationTitle" placeholder="Enter a title for your conversation">
        <div class="w-3/12">
            <button type="button" @click="createNamedConversation"
                class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                New Conversation
                <svg aria-hidden="true" class="w-5 h-5 ml-2 -mr-1" fill="currentColor" viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd"
                        d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                        clip-rule="evenodd"></path>
                </svg>
            </button>
        </div>
    </span>
    <div v-if="isEditingTitle"
        class="flex w-full justify-items-end items-center p-2 rounded-lg text-gray-900 text-white bg-blue-700 rounded dark:bg-blue-600">
        <input type="text"
            class="z-10 block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            v-model="newConversationTitle">
        <div @click="updateTitle(conversationId)" class="justify-self-end"
            v-if="store.currConversationId === conversationId && isEditingTitle">
            <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"
                aria-hidden="true" class="h-4 w-4" height="2em">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"></path>
            </svg>
        </div>
    </div>
    <div @click="setConversation(conversationId)" v-else-if="!isEditingTitle && conversationId !== 'new'"
        :class="`flex w-full justify-items-end items-center p-2 rounded-lg text-gray-900 ${store.currConversationId == conversationId ? 'text-white bg-blue-700 rounded dark:bg-blue-600' : 'dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700'}`">
        <svg aria-hidden="true" v-if="store.currConversationId !== conversationId"
            class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
            fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path d="M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z"></path>
            <path d="M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z"></path>
        </svg>
        <span class="ml-3">{{ title }}</span>
        <div @click="toggleEditTitle" class="justify-self-end"
            v-if="store.currConversationId === conversationId && !isEditingTitle">
            <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round"
                stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 20h9"></path>
                <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
            </svg>
        </div>
        <div @click="deleteConversation(conversationId)" class="justify-self-end" v-if="false">
            <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round"
                stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                <polyline points="3 6 5 6 21 6"></polyline>
                <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2">
                </path>
                <line x1="10" y1="11" x2="10" y2="17"></line>
                <line x1="14" y1="11" x2="14" y2="17"></line>
            </svg>
        </div>
    </div>
</template>