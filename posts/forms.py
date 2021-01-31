from django import forms
from .models import Post, Comment, Report

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'post_image')

        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control',}),
            'author': forms.TextInput(attrs={'class' : 'form-control','value': '' , 'id': 'authorID', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class' :  'form-control',}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body', )

        widgets = {
            'author': forms.TextInput(attrs={'class' : 'form-control','value': '' , 'id': 'authorID', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class' :  'form-control',}),
        }

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('author', 'body', )

        widgets = {
            'author': forms.TextInput(attrs={'class' : 'form-control','value': '' , 'id': 'authorID', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class' :  'form-control',}),
        }