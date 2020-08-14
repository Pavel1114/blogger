from django.urls import path

from apps.articles.views import ArticleDetailView

app_name = 'articles'

urlpatterns = [
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
]
