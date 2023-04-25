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

    def json_sans_chat_messages(self):
        conversation_dict = self.dict()
        conversation_dict.pop('chat_messages')
        return conversation_dict
    

class AutoGptSettings(BaseModel):
    ai_goals: str
    ai_name: str
    ai_role: str


class AutoGptMessage(BaseModel):
    role: str
    content: str

class AutoGptJson(BaseModel):
    texts: List[str]
    embeddings: List[list]
