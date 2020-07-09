from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import PostForm, CommentForm
from .models import Post, Comment

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class HomeView(ListView):
    """
    Renders a list of posts ordered by date on a home page
    """
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #('-pub_date' = DESC)
            # SELECT * FROM Post
            # WHERE published_date <= now
            # ORDER BY published_date DESC


class AboutView(TemplateView):
    """
    Renders /about page content
    """
    template_name = 'about.html'


class PostDetailView(DetailView):
    '''
    Renders post details
    '''
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    '''
    Renders a form to create a new post
    '''
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class UpdatePostView(LoginRequiredMixin, UpdateView):
    '''
    Renders a form to update an existing post
    '''
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class DeletePostView(LoginRequiredMixin, DeleteView):
    '''
    Renders a confirm_delete form
    '''
    model = Post
    success_url = reverse_lazy('blog:home')


class DraftListView(LoginRequiredMixin, ListView):
    '''
    Renders a list of unpublished posts
    '''
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')





