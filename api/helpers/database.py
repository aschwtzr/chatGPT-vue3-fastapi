from tinydb import TinyDB, Query
from tinydb.operations import set
from helpers.models import ChatMessage, Conversation
from helpers.utils import pp
from uuid import UUID
from fire import Fire

class DatabaseHelper:
    def create_new_conversation(self, conversation: Conversation):
        converjson = conversation.to_json()
        pp.pprint(f"{converjson =}")
        id = self.conversations.insert(converjson)
        self.conversations.update({'id': str(id)}, doc_ids=[id])
        return str(id)
    
    def add_message_to_conversation(self, conversation_id: str, chat_message: ChatMessage):
        Convo = Query()
        conversation = self.conversations.search(Convo.id == conversation_id)
        
        message_id = self.messages.insert(chat_message.dict())
        id_str = str(message_id)
        self.messages.update({'id': id_str}, doc_ids=[message_id])

        conversation[0]['chat_message_ids'].append(id_str)
        self.conversations.update(set('chat_message_ids', conversation[0]['chat_message_ids']), 
                                  Convo.id == conversation_id)
        return id_str

    def update_existing_message(self, message_id: str, chat_message: ChatMessage):
        Message = Query()
        conversation = self.conversations.search(Message.id == message_id)
        pp.pprint(f"{conversation = }")
        self.messages.update(chat_message.dict(), Message.id == message_id)

    def update_conversation_title(self, conversation_id: str, title: str):
        Convo = Query()
        conversation = self.conversations.search(Convo.id == conversation_id)
        pp.pprint(f"{conversation = }")
        # self.conversations.update({'title': title}, doc_ids=[conversation_id])
        self.conversations.update(set('title', title), Convo.id == conversation_id)

    def update_message_response(self, message_id: str, response: str):
        Message = Query()
        message = self.messages.search(Message.id == message_id)
        pp.pprint(f"{message[0] = }")
        self.messages.update(set('response', response), Message.id == message_id)

    def fetch_all_conversations(self):
        return self.conversations.all()
    
    def fetch_all_conversation_messages(self, conversation_id: str):
        Message = Query()
        messages = self.messages.search(Message.conversation_id == conversation_id)
        return messages

    def __init__(self, db_path: str = "./db.json"):
        self.db = TinyDB(db_path)
        self.conversations = self.db.table('conversations')
        self.messages = self.db.table('messages')

if __name__ == '__main__':
    db = DatabaseHelper('./db.json')
    all = db.conversations.all()
    pp.pprint(all)
    Fire(db)