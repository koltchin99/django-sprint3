from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.constants import LIMIT
from blog.models import Post, Category

def sort_post():
    return Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')


def index(request):
    template = 'blog/index.html'
    post_list = sort_post()[:LIMIT]

    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        sort_post(),
        id=post_id,
        pub_date__lte=timezone.now(),
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = sort_post().filter(category=category)

    context = {
        'post_list': post_list,
        'category': category,
    }
    return render(request, template, context)
