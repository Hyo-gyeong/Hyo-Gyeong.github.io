from django import forms 
from .models import Blog, Creator, Comment, CreatorComment, CommentReply, CreatorCommentReply


class New(forms.ModelForm): 
    class Meta: 
        model = Blog 
        fields = ['title','body','image'] 

class CreatorNew(forms.ModelForm): 
    class Meta: 
        model = Creator
        fields = ['title','body','image'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['contents']

class CreatorCommentForm(forms.ModelForm):
    class Meta:
        model = CreatorComment
        fields = ['ccontents']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ['contents']

class CreatorReplyForm(forms.ModelForm):
    class Meta:
        model = CreatorCommentReply
        fields = ['ccontents']