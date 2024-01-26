from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post

class PostTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username = 'Test User',
            email = 'test@example.com',
            password = 'Test Password',
        )

        cls.post = Post.objects.create(
            author = cls.user,
            title = 'Test Title',
            body = 'This is Test Body',
        )

    def test_post_model_content(self):
        self.assertEqual(self.post.title, 'Test Title')
        self.assertEqual(self.post.body, 'This is Test Body')
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(str(self.post), 'Test Title')
