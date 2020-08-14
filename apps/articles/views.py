from django.views.generic import DetailView, ListView

from apps.articles.models import Article


class IndexPageView(ListView):
    model = Article
    paginate_by = 30
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    model = Article
