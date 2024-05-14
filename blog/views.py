from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    published_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #ユーザからリクエストを受けたら、{}の中身をテンプレートにrender(表示する)
    return render(request, 'blog/post_list.html', {'published_posts': published_posts})
