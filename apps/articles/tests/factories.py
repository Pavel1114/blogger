from factory import DjangoModelFactory, Sequence
from factory.django import ImageField
from factory.faker import Faker


class ArticleFactory(DjangoModelFactory):
    title = Sequence(lambda n: f'Статья {n}')
    text = Faker('text', max_nb_chars=1000)
    image = ImageField()

    class Meta:
        model = 'articles.Article'
