from blog.models import Comment
from django.forms import ModelForm
from captcha.fields import ReCaptchaField


class CommentForm(ModelForm):
    recaptcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = '__all__'
