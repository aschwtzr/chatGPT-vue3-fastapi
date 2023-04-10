from pydantic import BaseModel, Field
from typing import Union, List

class ChatMessage(BaseModel):
    message: str
    response: Union[str, None] = None
    conversation_id: Union[str, None] = None
    id: Union[str, None] = None

class Conversation(BaseModel):
    id: Union[str, None] = None
    title: str = Field(default="Untitled Conversation")
    chat_messages: Union[List[ChatMessage], None] = []
    chat_message_ids: Union[List[str], None] = []

    def to_json(self):
        messages = [message.dict() for message in self.chat_messages]
        conversation_dict = self.dict()
        conversation_dict['chat_messages'] = messages
        return conversation_dict