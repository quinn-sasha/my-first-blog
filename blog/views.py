from django.views.generic import TemplateView


class PostListView(TemplateView):
    template_name = 'blog/post_list.html'
