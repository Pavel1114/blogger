from django.test import TestCase
from django.urls import reverse

from apps.articles.tests.factories import ArticleFactory


class ArticleDetailViewTestCase(TestCase):
    def test_detail_view(self):
        article = ArticleFactory()
        res = self.client.get(article.get_absolute_url())
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'articles/article_detail.html')
        self.assertIn('article', res.context_data)


class IndexPageViewTestCase(TestCase):
    def test_index_page_view(self):
        ArticleFactory.create_batch(10)
        res = self.client.get(reverse('home'))
        self.assertTemplateUsed(res, 'index.html')
        self.assertIn('article_list', res.context_data)
        self.assertEqual(len(res.context_data['article_list']), 10)
