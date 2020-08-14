from django.test import TestCase

from apps.articles.tests.factories import ArticleFactory


class ArticleModelTestCase(TestCase):
    def test_str(self):
        article = ArticleFactory()
        self.assertEqual(str(article), article.title)

    def test_get_absolute_url(self):
        article = ArticleFactory()
        self.assertEqual(article.get_absolute_url(), f'/articles/{article.pk}/')
