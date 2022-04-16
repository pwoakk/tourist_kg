from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .forms import CommentForm, PostCreateForm
from .models import Post, Category, Comment


# Create your views here.


def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'index.html', context=context)


def get_post_list(request, slug=None):
    if slug is not None:
        posts = Post.objects.filter(category__slug=slug, is_active=True)
    else:
        posts = Post.objects.filter(is_active=True)
    context = {
        "posts" : posts,
    }
    return render(request, 'post_list.html', context=context)


def get_post_detail_list(request, **kwargs):

    try:
        post_id = kwargs['pk']
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post_id)

    except Post.DoesNotExist:
        raise Http404()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.post = post
            instance.save()
        return redirect("post_detail_list", pk=post.id)   # redirect - перенаправление на указанную страницу
    else:
        form = CommentForm()
    context = {
        "post": post,
        "form": form,
        "comments": comments
    }
    return render(request, 'post_detail.html', context=context)


class PostCreateView(LoginRequiredMixin, FormView):
    template_name = 'post_create.html'
    form_class = PostCreateForm
    success_url = '/'
    login_url = 'sign_in'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return super().form_valid(form)