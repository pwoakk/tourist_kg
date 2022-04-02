from django.db.models import Count


from post.models import Category


def post_category(request):
    return {"category_list": Category.objects.annotate(article_count=Count('posts'))}


