from django.contrib import admin
from .models import Blog
from .models import Creator
from .models import Comment
from .models import CreatorComment

# Register your models here.
admin.site.register(Blog)
admin.site.register(Creator)
admin.site.register(Comment)
admin.site.register(CreatorComment)
