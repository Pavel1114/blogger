from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, ListView

from apps.articles.forms import ArticleModelForm
from apps.articles.models import Article


class IndexPageView(ListView):
    model = Article
    paginate_by = 30
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    model = Article


class ArticleAddView(SuccessMessageMixin, CreateView):
    model = Article
    template_name = 'articles/article_add.html'
    form_class = ArticleModelForm
    success_message = 'Статья добавлена'

    def form_valid(self, form):
        article = form.save(commit=False)
        if self.request.user.is_authenticated:
            article.author = self.request.user
        article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()
