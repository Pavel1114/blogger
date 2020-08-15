from django.urls import path

from apps.articles.views import ArticleAddView, ArticleDetailView

app_name = 'articles'

urlpatterns = [
    path("add/", ArticleAddView.as_view(), name="article_add"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
]
