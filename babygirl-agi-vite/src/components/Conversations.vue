<script setup>
import { onMounted, ref } from 'vue'
import ConversationButton from './ConversationButton.vue'
import { 
    getAllConversations
} from '../api/babygirl-api'
import { store } from '../store.js'

const isEditingTitle = ref(false)
onMounted(() => {
    getAllConversations().then((res) => {
        console.log(res)
        store.conversations = res
    })
})


</script>
<template>
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
</template>