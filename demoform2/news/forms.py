from django import forms
from .models import Post


class PostForm(forms.ModelForm): # Form based on Model
    class Meta:
        model = Post
        fields = ('title', 'content', 'time_create',)
        widget = {
            'title' : forms.Textarea(attrs= {'class': 'tieude123'}), #Set ClassName = tieude123 by Widget
            'content': forms.Textarea(attrs={'class': 'noidung123'}),
        }


class SendEmail(forms.Form): # Form based on Yourself
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs= {'class': 'tieude'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs= {'class': 'tuantran', 'id': 'noidung'})) # Build to Textarea
    cc = forms.BooleanField(required=False)