from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from helpers.chat_helper import ChatHelper
from helpers.models import ChatMessage, Conversation

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chat_helper = ChatHelper()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/conversation")
def read_all_conversations():
    return chat_helper.fetch_all_conversations()

@app.post("/conversation")
def create_new_conversation(conversation: Conversation):
    conversation_dict = chat_helper.create_new_conversation(conversation)
    return conversation_dict

@app.get("/conversation/{conversation_id}/messages")
def read_conversation(conversation_id: str):
    return chat_helper.fetch_all_conversation_messages(conversation_id)

# ONLY UPDATE THE CONVERSATION TITLE
@app.patch("/conversation/{conversation_id}")
def update_conversation(conversation_id: str, conversation: Conversation):
    chat_helper.update_conversation_title(conversation_id, conversation.title)
    return conversation.dict()

@app.post("/message")
def create_new_chat(chat_message: ChatMessage):
    chat_message_dict = chat_helper.add_message_to_conversation(chat_message.conversation_id, chat_message)
    chat_message_dict = chat_helper.add_message_to_conversation(chat_message.conversation_id,
                                                                 chat_message)
    return chat_message_dict
