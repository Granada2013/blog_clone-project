from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
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
        return Post.objects.filter(published_date__lte=timezone.now()).order_by(
            '-published_date')  # ('-pub_date' = DESC)
        # SELECT * FROM Post
        # WHERE published_date <= now
        # ORDER BY published_date DESC


class AboutView(TemplateView):
    """
    Renders /about page content
    """
    template_name = 'about.html'


class PostDetailView(DetailView):
    """
    Renders post details
    """
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    """
    Renders a form to create a new post
    """
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class UpdatePostView(LoginRequiredMixin, UpdateView):
    """
    Renders a form to update an existing post
    """
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class DeletePostView(LoginRequiredMixin, DeleteView):
    """
    Renders a confirm_delete form
    """
    model = Post
    success_url = reverse_lazy('blog:home')


class DraftListView(LoginRequiredMixin, ListView):
    """
    Renders a list of unpublished posts
    """
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


@login_required
def publish_post(request, pk):
    """
    Realizes .publish() method of class Post
    """
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:home', pk=pk)


def add_comment(request, pk):
    """
    Renders a comment form and saves a new comment to a database
    """
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def approve_comment(request, pk):
    """
    Realizes the .approve() metnod of class Comment
    """
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog:post_detail', pk=comment.post.pk)


@login_required
def remove_comment(request, pk):
    """
    Realizes built-in .delete() method of class Comment
    """
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail', pk=post_pk)
