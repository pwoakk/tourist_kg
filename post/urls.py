from django.urls import path
from .views import index, get_post_list, get_post_detail_list, PostCreateView

urlpatterns = [
    path('', index, name='index'),
    path('blog/posts/', get_post_list, name='post_list'),
    path('blog/posts/<int:pk>/', get_post_detail_list, name='post_detail_list'),
    path('blog/category/<slug:slug>/', get_post_list, name='category_posts'),
    path('blog/post/create/', PostCreateView.as_view(), name='name_create'),
]
