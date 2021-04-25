from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post
# Create your tests here.


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='currywurst',
        )

        self.post = Post.objects.create(
            title='Dutchman',
            slug='defaults',
            author= self.user,
            content='Germany is a very good country to travel to',
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/defaults/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Dutchman')
        self.assertEqual(f'{self.post.slug}', 'defaults')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.content}', 'Germany is a very good country to travel to')


    def test_post_create_view(self):  # new
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'slug': 'New title',
            'author': self.user.id,
            'content': 'new text',
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'Dutchman')
        self.assertEqual(Post.objects.last().slug, 'defaults')
        self.assertEqual(Post.objects.last().content, 'Germany is a very good country to travel to')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'content': 'Updated text',
        })

        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(
            reverse('post_delete', args='1'))

        self.assertEqual(response.status_code, 302)