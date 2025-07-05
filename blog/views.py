from django.shortcuts import render,redirect
from . models import Category,Blog,Comment
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

def home(request):
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True)
    non_featured_post = Blog.objects.filter(is_featured=False,status='Published')
    return render(request,'blog/home-blogs.html',{'categories':categories,'featured_post':featured_post,'non_featured_post':non_featured_post})


def get_post_by_category(request,category_id):
    categories = Category.objects.all()
    post = Blog.objects.filter(status='Published',category_id=category_id)
    return render(request,'blog/get_post_by_category.html',{'post':post,'categories':categories})

def single_post(request,pk):
    categories = Category.objects.all()
    post = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = post
        comment.comment = request.POST['comment']
        comment.save()
        return redirect('single_post',pk=post.pk)

    comments = Comment.objects.filter(blog=post)
    comments_count = comments.count()
    
    context = {
        'post':post,
        'categories':categories,
        'comments':comments,
        'comments_count':comments_count
    }
    return render(request,'blog/single_post.html',context)


def search(request):
    keyword = request.GET.get('keyword')
    post = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_desc__icontains=keyword) | Q(blog_body__icontains=keyword))
    
    categories = Category.objects.all()
    context = {
        'categories':categories,
        'post':post,
        'keyword':keyword
    }
    return render(request,'blog/search.html',context)