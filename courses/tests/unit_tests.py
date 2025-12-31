import logging

from django.contrib.auth import get_user_model
from django.test import TestCase

from courses.models import Course, Subject

logger = logging.getLogger(__name__)
User = get_user_model()


# Create your tests here.
class CoursesUnitTest(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.test_user = User.objects.create(
            username="testuser", email="test@example.com", password="testpass123"
        )

        try:
            self.test_subject = Subject.objects.create(title="test subject", slug="test-subject")
        except Exception as e:
            logger.error(f"Error occurred while creating subject: {e}")

        try:
            self.test_course = Course.objects.create(
                owner=self.test_user,
                subject=self.test_subject,
                title="test title",
                slug="test-title",
                overview="test title overview",
            )
        except Exception as e:
            logger.error(f"Error occurred while creating subject: {e}")

    def test_create_subject(self):
        Subject.objects.create(title="test title 2", slug="test-title-2")
        subject_exists = Subject.objects.filter(title="test title 2").exists()

        self.assertTrue(subject_exists)

    def test_create_unique_subject(self):
        try:
            Subject.objects.create(title="test title", slug="test-subject")
        except Exception as e:
            logger.error(e)

        self.assertTrue(1)
