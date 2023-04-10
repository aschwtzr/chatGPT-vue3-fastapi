from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from helpers.openapi import send_openai_chat_message
from helpers.utils import pp
from helpers.models import ChatMessage, Conversation
from helpers.database import DatabaseHelper
chat_db = DatabaseHelper('../db.json')

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

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/conversation")
def read_all_conversations():
    return chat_db.fetch_all_conversations()

@app.post("/conversation")
def create_new_conversation(conversation: Conversation):
    pp.pprint(conversation.dict())
    conversation.id = chat_db.create_new_conversation(conversation)
    # should only be one message at this time
    for chat in conversation.chat_messages:
        chat_db.add_message_to_conversation(conversation.id, chat.message)
    return conversation.dict()

@app.get("/conversation/{conversation_id}/messages")
def read_conversation(conversation_id: str):
    return chat_db.fetch_all_conversation_messages(conversation_id)

# ONLY UPDATE THE CONVERSATION TITLE
@app.patch("/conversation/{conversation_id}")
def update_conversation(conversation_id: str, conversation: Conversation):
    chat_db.update_conversation_title(conversation_id, conversation.title)
    response = 'updating'
    return response

@app.post("/message")
def create_new_chat(chat_message: ChatMessage):
    chat_message.id = chat_db.add_message_to_conversation(chat_message.conversation_id, chat_message)
    # chat_message.response = send_openai_chat_message(chat_message.message)
    chat_message.response = "Testing response save"
    chat_db.update_message_response(chat_message.id, chat_message.response)
    return chat_message.dict()