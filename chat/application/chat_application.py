# app/chat/application/chat_application.py

from app.chat.domain.chat_domain import Chat

class ChatApplication:
    def __init__(self):
        self.chat = Chat()

    def send_message(self, message):
        self.chat.send_message(message)

    def get_messages(self):
        return self.chat.get_messages()