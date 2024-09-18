import unittest
from messaging.domain.services.messaging_service import MessagingService

class TestMessaging(unittest.TestCase):
    def setUp(self):
        self.messaging_service = MessagingService()

    def test_send_message(self):
        # Test sending a message
        message = "Hello, world!"
        result = self.messaging_service.send_message(message)
        self.assertTrue(result)

    def test_receive_message(self):
        # Test receiving a message
        message = self.messaging_service.receive_message()
        self.assertIsNotNone(message)

if __name__ == '__main__':
    unittest.main()