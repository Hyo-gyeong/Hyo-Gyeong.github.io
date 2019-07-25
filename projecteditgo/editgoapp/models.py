from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to = 'images/', blank = True, null = True)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def sum(self):
        return self.body[:40]

class Creator(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to = 'image/',  blank = True, null = True)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def sum(self):
        return self.body[:50]

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, null = True, related_name = 'comments')
    contents = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.contents


class CreatorComment(models.Model):
    creator = models.ForeignKey(Creator, on_delete = models.CASCADE, null = True, related_name = 'ccomments')
    ccontents = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.ccontents

class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replys', null=True)
    contents = models.CharField(max_length=500)

    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.contents

class CreatorCommentReply(models.Model):
    ccomment = models.ForeignKey(CreatorComment, on_delete=models.CASCADE, related_name='creplys', null=True)
    ccontents = models.CharField(max_length=500)

    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.ccontents