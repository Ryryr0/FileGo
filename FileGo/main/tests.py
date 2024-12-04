import os

from django.conf import settings
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from main import views
from posts.models import Post


class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('main:home')
        self.assertEqual(resolve(url).func.view_class, views.NewsLine)

    def test_search_home_url_resolves(self):
        url = reverse('main:search_home', kwargs={'q': 'test'})
        self.assertEqual(resolve(url).func.view_class, views.NewsLine)


class TestNewsLineView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='password123')

        cls.post1 = Post.objects.create(
            title='Test Post 1', content='Content of post 1', author=cls.user, is_published=True
        )
        cls.post2 = Post.objects.create(
            title='Another Test Post', content='Content of post 2', author=cls.user, is_published=True
        )

    def test_newsline_view_all_posts(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertIn(self.post1, response.context['posts'])
        self.assertIn(self.post2, response.context['posts'])

    def test_newsline_view_search(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('main:search_home', kwargs={'q': 'Another'}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.post2, response.context['posts'])
        self.assertIn(self.post1, response.context['posts'])

    def test_newsline_search_elim_words(self):
        self.client.login(username='testuser', password='password123')

        elim_words_file = os.path.join(settings.BASE_DIR, 'utils', 'strings', 'search_elim_words_en.text')
        with open(elim_words_file, 'w') as f:
            f.write('Another')

        response = self.client.get(reverse('main:search_home', kwargs={'q': 'Another Test'}))
        self.assertEqual(response.status_code, 200)

        self.assertIn(self.post2, response.context['posts'])

    def test_newsline_view_context(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.context['user_name'], 'testuser')
        self.assertEqual(response.context['search_field'], '')

