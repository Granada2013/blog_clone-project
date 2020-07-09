from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.UpdatePostView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove', views.DeletePostView.as_view(), name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
]