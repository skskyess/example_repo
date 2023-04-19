from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Имена участников')
    description = forms.CharField(label='Ссылка на гуглдиск, где расписан ваш старптап')
    cost = forms.CharField(label='номер лидера команды')
    class Meta:
        model = Post
        fields = ('title', 'description','cost',)
