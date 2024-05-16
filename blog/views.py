from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    published_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #ユーザからリクエストを受けたら、{}の中身をテンプレートにrender(表示する)
    return render(request, 'blog/post_list.html', {'published_posts': published_posts})
def post_detail(request, pk):
    published_post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'published_post': published_post})

