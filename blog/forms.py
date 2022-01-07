from django import forms
from .models import Message, Comment


class SendMessage(forms.ModelForm):
    article = forms.CharField(
        label='Тема письма',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Ваш email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    text = forms.CharField(
        label='Текст сообщения',
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Message
        fields = ['article', 'email', 'text']


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        label='Cообщение*',
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    # user = forms.CharField(
    #     label='Пользователь',
    #     required=True,
    #     widget=forms.HiddenInput()
    # )
    # title = forms.CharField(
    #     label='Статья',
    #     required=True,
    #     widget=forms.HiddenInput()
    # )

    class Meta:
        model = Comment
        fields = ['text']