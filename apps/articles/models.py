from django.db.models import SET_NULL, CharField, ForeignKey, ImageField, TextField
from django.urls import reverse
from model_utils.models import TimeStampedModel


class Article(TimeStampedModel):
    title = CharField("Название", max_length=1000)
    text = TextField("Текст")
    image = ImageField("изображение", upload_to="articles/%Y/%m/")
    author = ForeignKey("users.User", verbose_name="автор", on_delete=SET_NULL, null=True, editable=False)

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article_detail', kwargs={'pk': self.pk})
