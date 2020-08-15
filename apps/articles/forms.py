from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Field, Layout, Submit
from django.forms import CharField, FileInput, ModelForm, Textarea

from apps.articles.models import Article


class ImageInputWithPreview(FileInput):
    class Media:
        js = ['js/widgets/image_input_with_preview.js']


class ArticleModelForm(ModelForm):
    helper = FormHelper()
    helper.include_media = False
    helper.layout = Layout(
        Div(
            Div(
                Field('title', placeholder='Введите название статьи', tabindex=1),
                css_class='col-sm-8'
            ),
            Div(Field('text', tabindex=2, css_class='js-wysiwyg'),
                css_class='col-sm-8 order-sm-1'),
            Div(
                Div(
                    HTML(
                        '<h5 class="text-primary text-center font-family-circle-rounded">'
                        'Загрузить изображение</h5>'),
                    Field('image', template='common/form_layouts/image_with_preview.html', tabindex=3),
                    css_class='border h-100 p-2'
                ),
                css_class='col-sm-4 form-group order-sm-1'
            ),
            Div(
                Div(
                    Submit('Submit', 'Опубликовать', type='Submit', tabindex=4,
                           css_class='btn btn-danger btn-block font-family-museo-cyrl-900'),
                    css_class='d-sm-inline-block'
                ),
                css_class='col-sm-4'
            ),
            css_class='row align-items-lg-stretch'),
    )

    text = CharField(min_length=30, widget=Textarea,
                     error_messages={'min_length': 'минимальный размер статьи 30 символов'})

    class Meta:
        model = Article
        fields = ('title', 'text', 'image')
        error_messages = {
            'image': {
                'required': 'изображение обязательно'
            },
        }
        widgets = {
            'image': ImageInputWithPreview
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['text'].label = ''
