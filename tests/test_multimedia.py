import unittest

from app.multimedia.domain.multimedia_domain import Multimedia
from app.multimedia.application.multimedia_application import MultimediaService
from app.multimedia.infrastructure.multimedia_infrastructure import MultimediaRepository

class MultimediaServiceTest(unittest.TestCase):
    def setUp(self):
        self.repository = MultimediaRepository()
        self.service = MultimediaService(self.repository)

    def test_create_multimedia(self):
        multimedia = Multimedia(name="example.mp4", size=1024)
        created_multimedia = self.service.create_multimedia(multimedia)
        self.assertEqual(created_multimedia.name, "example.mp4")
        self.assertEqual(created_multimedia.size, 1024)

    def test_get_multimedia(self):
        multimedia = Multimedia(name="example.mp4", size=1024)
        self.repository.save(multimedia)
        retrieved_multimedia = self.service.get_multimedia(multimedia.id)
        self.assertEqual(retrieved_multimedia.name, "example.mp4")
        self.assertEqual(retrieved_multimedia.size, 1024)

    def test_delete_multimedia(self):
        multimedia = Multimedia(name="example.mp4", size=1024)
        self.repository.save(multimedia)
        self.service.delete_multimedia(multimedia.id)
        self.assertIsNone(self.repository.get(multimedia.id))

if __name__ == "__main__":
    unittest.main()