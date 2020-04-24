from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post
from .forms import PostForm, RegistrationForm
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form, 'title': post.title})

def register_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
            return HttpResponseRedirect('/')
        else:
            return render(request, 'registration/register.html', {'form': form, 'answer': "User is already exist or bad data."})
    form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_posts(request, us):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'post_list.html', {'posts': posts})

def search(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == 'GET':
        posts = Post.objects.filter(title__icontains=request.GET.get('query'))
    return render(request, 'post_list.html', {'posts': posts})

def post_delete(request, pk):
    post = Post.objects.filter(pk=pk).delete()
    return render(request, 'post_delete.html')