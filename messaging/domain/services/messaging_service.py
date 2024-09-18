# app/messaging/domain/services/messaging_service.py

class MessagingService:
    def __init__(self, messaging_adapter):
        self.messaging_adapter = messaging_adapter

    def send_message(self, message):
        self.messaging_adapter.send_message(message)

    def receive_message(self):
        return self.messaging_adapter.receive_message()