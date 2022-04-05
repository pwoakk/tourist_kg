from django.db.models import Count


from post.models import Category


def post_category(request):
    # return {"category_list": Category.objects.annotate(article_count=Count('posts'))}
    # второй вариант не используя annotate, считая в html через category.posts.all.count
    return {"categories": Category.objects.all()}


