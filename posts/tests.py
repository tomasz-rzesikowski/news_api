from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from posts.models import Post


class PostModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        user = User.objects.create_user(username='John', password='password123')
        Post.objects.create(author=user, title='first post', body='a body here')

    def test_author_content(self):
        post = Post.objects.last()
        expected_author_username = f'{post.author.username}'
        self.assertEqual(expected_author_username, 'John')

    def test_title_content(self):
        post = Post.objects.last()
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'first post')

    def test_title_body(self):
        post = Post.objects.last()
        expected_object_body = f'{post.body}'
        self.assertEqual(expected_object_body, 'a body here')