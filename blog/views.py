from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    published_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #ユーザからリクエストを受けたら、{}の中身をテンプレートにrender(表示する)
    return render(request, 'blog/post_list.html', {'published_posts': published_posts})

def post_detail(request, pk):
    published_post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'published_post': published_post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            published_post = form.save(commit=False)
            published_post.author = request.user
            published_post.published_date = timezone.now()
            published_post.save()
            return redirect('post_detail', pk=published_post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    published_post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=published_post)
        published_post = form.save(commit=False)
        published_post.author = request.user
        published_post.published_date = timezone.now()
        published_post.save()
        return redirect('post_detail', pk=published_post.pk)
    else:
        form = PostForm(instance=published_post)
    return render(request, 'blog/post_edit.html', {'form': form})


