from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime
from .models import Blog, Creator, Comment, CreatorComment, CommentReply, CreatorCommentReply
from .forms import New, CreatorNew, CommentForm, CreatorCommentForm, ReplyForm, CreatorReplyForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    return render(request, 'home.html')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def creatordetail(request, creator_id):
    creator_detail = get_object_or_404(Creator, pk = creator_id)
    return render(request, 'creatordetail.html', {'creator': creator_detail})

def editor(request):
    blogs = Blog.objects

    editor_list = Blog.objects.all()
    paginator = Paginator(editor_list, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.get_page(1)

    return render(request, 'editor.html', {'blogs':blogs, 'posts':posts})

def creator(request):
    creator_blog = Creator.objects

    creator_list = Creator.objects.all()
    paginator = Paginator(creator_list, 6)
    page = request.GET.get('page')
    try:
        cposts = paginator.get_page(page)
    except PageNotAnInteger:
        cposts = paginator.get_page(1)
        
    return render(request, 'creator.html', {'creatorblog':creator_blog, 'cposts':cposts})
    

def editorform(request):
    
     # 1. 입력된 내용 처리 : POST
    if request.method == 'POST':
        form = New(request.POST, request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
        return redirect('editor')
            
    # 2. 빈 페이지 띄워주는 기능 : GET
    else:
        form = New()
        return render(request, 'editorform.html', {'form': form}) 

        
    
def creatorform(request):

     # 1. 입력된 내용 처리 : POST
    if request.method == 'POST':
        cform = CreatorNew(request.POST, request.FILES)
        if cform.is_valid(): 
            cpost = cform.save(commit=False)
            cpost.pub_date = timezone.now()
            cpost.save()
        return redirect('creator')
            
    # 2. 빈 페이지 띄워주는 기능 : GET
    else:
        cform = CreatorNew()
        return render(request, 'creatorform.html', {'cform': cform})     


def mypage(request):
    return render(request, 'mypage.html')


def delete(request, blog_id):
    blog = get_object_or_404 (Blog, pk = blog_id)
    blog.delete()

    return redirect('editor')


def creatordelete(request, creator_id):
    creator = get_object_or_404 (Creator, pk = creator_id)
    creator.delete()

    return redirect('creator')



def comment_create(request, blog_id):

        if request.method == 'POST':
                blog = get_object_or_404(Blog, pk=blog_id)
                form = CommentForm(request.POST)

                if form.is_valid():
                        comment = form.save(commit = False)
                        comment.blog = blog
                        comment.save()
                return redirect('/blog/' + str(blog.id))
        else:
                form = CommentForm()
                return render(request, 'detail.html', {'form' : form})

def comment_delete(request, blog_id, comment_id):

        blog = get_object_or_404(Blog, pk=blog_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.delete()
        
        return redirect('/blog/' + str(blog.id))



def creatorcomment_create(request, creator_id):

        if request.method == 'POST':
                creator = get_object_or_404(Creator, pk=creator_id)
                cform = CreatorCommentForm(request.POST)

                if cform.is_valid():
                        ccomment = cform.save(commit = False)
                        ccomment.creator = creator
                        ccomment.save()
                return redirect('/creator/' + str(creator.id))
        else:
                cform = CreatorCommentForm()
                return render(request, 'creatordetail.html', {'cform' : cform})

def creatorcomment_delete(request, creator_id, ccomment_id):

        creator = get_object_or_404(Creator, pk=creator_id)
        ccomment = get_object_or_404(CreatorComment, pk=ccomment_id)
        ccomment.delete()
        
        return redirect('/creator/' + str(creator.id))


def comment_reply(request, blog_id, comment_id):

        if request.method == 'POST':
                comment = get_object_or_404(Comment, pk=comment_id)
                reform = ReplyForm(request.POST)

                if reform.is_valid():
                        reply = reform.save(commit = False)
                        reply.comment = comment
                        reply.save()
                return redirect('/blog/' + str(blog_id))
        else:
                reform = ReplyForm()
                return render(request, 'detail.html', {'reform' : reform})


def comment_reply_delete(request, blog_id, comment_id, commentReply_id):

        blog = get_object_or_404(Blog, pk=blog_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        commentReply = get_object_or_404(CommentReply, pk=commentReply_id)
        commentReply.delete()
        
        return redirect('/blog/' + str(blog.id))

def creator_comment_reply(request, creator_id, ccomment_id):

        if request.method == 'POST':
                ccomment = get_object_or_404(CreatorComment, pk=ccomment_id)
                creform = CreatorReplyForm(request.POST)

                if creform.is_valid():
                        creply = creform.save(commit = False)
                        creply.ccomment = ccomment
                        creply.save()
                return redirect('/creator/' + str(creator_id))
        else:
                creform = CreatorReplyForm()
                return render(request, 'creatordetail.html', {'creform' : creform})


def creator_comment_reply_delete(request, creator_id, ccomment_id, ccommentReply_id):
        
        creator = get_object_or_404(Creator, pk=creator_id)
        ccomment = get_object_or_404(CreatorComment, pk=ccomment_id)
        ccommentReply = get_object_or_404(CreatorCommentReply, pk=ccommentReply_id)
        ccommentReply.delete()
        
        return redirect('/creator/' + str(creator.id))