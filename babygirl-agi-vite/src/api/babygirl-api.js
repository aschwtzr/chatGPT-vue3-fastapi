import axios from 'axios'

export const updateConversationTitle = async (id, title) => {
    const errored = false
    const loading = true
    return new Promise((resolve, reject) => {
        const res = axios
            .patch(`http://localhost:8000/conversation/${id}`, { id, title })
            .then(response => {
                resolve(response.data)
            })
            .catch(error => {
                reject(error)
            })
            .finally(() => {
                console.log('done')
            })

    })
}

export const getAllConversations = async () => {
    const errored = false
    const loading = true
    return new Promise((resolve, reject) => {
        const res = axios
            .get('http://localhost:8000/conversation')
            .then(response => {
                resolve(response.data)
            })
            .catch(error => {
                reject(error)
            })
            .finally(() => {
                console.log('done')
            })

    })
}

export const createNewNamedConversation = async (title) => {
    const errored = false
    const loading = true
    
    return new Promise((resolve, reject) => {
        const res = axios
            .post('http://localhost:8000/conversation', { title })
            .then(response => {
                resolve(response.data)
            })
            .catch(error => {
                reject(error)
            })
            .finally(() => {
                console.log('done')
            })

    })
}


export const createNewConversation = async (message) => {
    const errored = false
    const loading = true
    
    return new Promise((resolve, reject) => {
        const res = axios
            .post('http://localhost:8000/conversation', { title: 'Untitled Conversation', chat_messages: [{ message }] })
            .then(response => {
                resolve(response.data)
            })
            .catch(error => {
                reject(error)
            })
            .finally(() => {
                console.log('done')
            })

    })
}

export const postConversationMessage = async (conversation_id, message) => {
    const errored = false
    const loading = true
    return new Promise((resolve, reject) => {
        const res = axios
            .post('http://localhost:8000/message', { conversation_id, message })
            .then(response => {
                resolve(response.data)
            })
            .catch(error => {
                reject(error)
            })
            .finally(() => {
                console.log('done')
            })

    })
}

export const getConversationMessages = async (id) => {
    const errored = false
    const loading = true
    return new Promise((resolve, reject) => {
        const res = axios
            .get(`http://localhost:8000/conversation/${id}/messages`)
            .then(response => {
                resolve(response.data)
            })
            .catch(error => {
                reject(error)
            })
            .finally(() => {
                console.log('done')
            })

    })
}