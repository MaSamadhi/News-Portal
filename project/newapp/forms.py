from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    postText = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'postAuthor',
            'postTitle',
            'postText',
            'postCategory',
        ]

    def clean(self):
        cleaned_data = super().clean()
        postTitle = cleaned_data.get("postTitle")
        postText = cleaned_data.get("postText")

        if postTitle == postText:
            raise ValidationError(
                "Текст статьи не должен быть идентичен заголовку."
            )
        return cleaned_data