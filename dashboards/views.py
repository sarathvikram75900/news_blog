from django.shortcuts import render,redirect
from blog.models import Category,Blog
from django.contrib.auth.decorators import login_required
from . forms import CategoryForm,BlogForm,UserForm,EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    categories = Category.objects.all()
    categories_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        'categories':categories,
        'categories_count':categories_count,
        'blogs_count':blogs_count

    }
    return render(request,'dashboards/dashboard.html',context)


def categories(request):
    categories = Category.objects.all().order_by('-created_at')
    context = {
        'categories':categories,
        }
    return render(request,'dashboards/categories.html',context)


def add_categories(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    categories = Category.objects.all()
    form = CategoryForm()
    context = {
        'categories':categories,
        'form' : form,
    }
    return render(request,'dashboards/add_categories.html',context)


def edit_category(request,pk):
    categories = Category.objects.all()
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'categories':categories,
        'form' : form,
    }
    return render(request,'dashboards/edit_category.html',context)


def delete_category(request,pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('categories')



def posts(request):
    categories = Category.objects.all()
    posts = Blog.objects.all()
    context = {
        'categories':categories,
        'posts':posts
    }
    return render(request,'dashboards/posts.html',context)


def add_posts(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            return redirect('posts')
    categories = Category.objects.all()
    form = BlogForm()
    context = {
        'categories':categories,
        'form':form
    }

    return render(request,'dashboards/add_posts.html',context)



def edit_posts(request,pk):
    posts = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance=posts)
        if form.is_valid():
            post = form.save(commit=False)
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            return redirect('posts')
    form = BlogForm(instance=posts)
    categories = Category.objects.all()
    context = {
        'categories':categories,
        
        'form':form
    }
    return render(request,'dashboards/edit_posts.html',context)


def delete_posts(request,pk):
    posts = Blog.objects.get(pk=pk)
    posts.delete()
    return redirect('posts')



def users(request):
    categories = Category.objects.all()
    users = User.objects.all()
    context = {
        'categories' : categories,
        'users' : users
    }
    return render(request,'dashboards/users.html',context)


def add_users(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = UserForm()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'form':form
    }
    return render(request,'dashboards/add_users.html',context)

def edit_user(request,pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    
    form = EditUserForm(instance=user)
    categories = Category.objects.all()
    context = {
        'form':form,
        'categories':categories
    }
    return render(request,'dashboards/edit_user.html',context)

def delete_user(request,pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('users')