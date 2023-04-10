import { reactive } from 'vue'

export const store = reactive({
    currConversationId: '',
    conversations: [],
    conversationMessages: [],
    updateconversationMessages(message) {
        this.conversationMessages.push(message)
    },
    setCurrentConversation(convoId) {
        console.log(convoId)
        this.currConversationId = convoId
    },
    currentConversation() {
        return this.conversations.find(convo => convo.id === this.currConversationId)
    },
    updateConversationTitle(title) {
        const currentIdx = this.conversations.findIndex(convo => convo.id === this.currConversationId)
        const copy = [...this.conversations]
        copy[currentIdx].title = title
        this.conversations = [...copy]
    }
})