from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(
        label="内容",
        widget=forms.Textarea(attrs={'placeholder': 'その気持ち、シェアしましょう'})
        )
    
    class Meta:
        model = Post
        fields = ['content']