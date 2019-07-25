from django.contrib import admin
from django.urls import path, include
import editgoapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', editgoapp.views.home, name="home"),
    path('blog/editor/', editgoapp.views.editor, name="editor"),
    path('blog/<int:blog_id>', editgoapp.views.detail, name="detail"),
    path('creator/<int:creator_id>', editgoapp.views.creatordetail, name="creatordetail"),
    path('blog/creator/', editgoapp.views.creator, name="creator"),
    path('blog/mypage/', editgoapp.views.mypage, name="mypage"),
    path('blog/editorform/', editgoapp.views.editorform, name="editorform"),
    path('blog/creatorform/', editgoapp.views.creatorform, name="creatorform"),
    path('blog/delete/<int:blog_id>', editgoapp.views.delete, name="delete"),
    path('creator/creatordelete/<int:creator_id>', editgoapp.views.creatordelete, name="creatordelete"),
    path('accounts/', include('allauth.urls')),
    path('<int:blog_id>/comment', editgoapp.views.comment_create, name="comment_create"),
    path('<int:blog_id>/comment/<int:comment_id>/delete', editgoapp.views.comment_delete, name="comment_delete"),
    path('creator/<int:creator_id>/ccomment', editgoapp.views.creatorcomment_create, name="creatorcomment_create"),
    path('creator/<int:creator_id>/ccomment/<int:ccomment_id>/creatorcomment_delete', editgoapp.views.creatorcomment_delete, name="creatorcomment_delete"),
    path('<int:blog_id>/comment/<int:comment_id>/comment_reply', editgoapp.views.comment_reply, name="comment_reply"),
    path('<int:blog_id>/comment/<int:comment_id>/delete/<int:commentReply_id>/comment_reply_delete', editgoapp.views.comment_reply_delete, name="comment_reply_delete"),
    path('creator/<int:creator_id>/ccomment/<int:ccomment_id>/creator_comment_reply', editgoapp.views.creator_comment_reply, name="creator_comment_reply"),
    path('creator/<int:creator_id>/ccomment/<int:ccomment_id>/creatorcomment_delete/<int:ccommentReply_id>/creator_comment_reply_delete', editgoapp.views.creator_comment_reply_delete, name="creator_comment_reply_delete"),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
