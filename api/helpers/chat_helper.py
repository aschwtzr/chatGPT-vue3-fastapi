from helpers.database import DatabaseHelper
from helpers.models import ChatMessage, Conversation
from helpers.utils import pp
from helpers.openapi import send_openai_chat_message

chat_db = DatabaseHelper('../db.json')
class ChatHelper():
    def create_new_conversation(self, conversation: Conversation) -> dict:
        conversation.id = chat_db.create_new_conversation(conversation)
        pp.pprint(conversation.dict())
        # should only be one message at this time
        chat_messages = [
            self.add_message_to_conversation(conversation.id, chat_message)
            for chat_message in conversation.chat_messages
                         ]
        response_dict = conversation.dict()
        response_dict['chat_messages'] = chat_messages.dict()
        return response_dict
    
    def fetch_all_conversations(self) -> list:
        return chat_db.fetch_all_conversations()
    
    def fetch_all_conversation_messages(self, conversation_id: str) -> list:
        return chat_db.fetch_all_conversation_messages(conversation_id)
    
    def update_conversation_title(self, conversation_id: str, title: str) -> None:
        chat_db.update_conversation_title(conversation_id, title)

    def add_message_to_conversation(self, conversation_id: str, chat_message: ChatMessage) -> dict:
        # separate the message and response save below if needed
        # chat_message.id = chat_db.add_message_to_conversation(conversation_id, chat_message)
        
        # chat_message.response = send_openai_chat_message(chat_message.message)
        chat_message.response = "TESTING RESPONSE STRING"

        chat_message.id = chat_db.add_message_to_conversation(conversation_id, chat_message)
        # chat_db.update_message_response(chat_message.id, chat_message.response)
        return chat_message.dict()

    def __init__(self) -> None:
        pass
