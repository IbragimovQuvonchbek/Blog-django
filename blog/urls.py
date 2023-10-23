from .views import BlogPostViwes, FullPostViews, CreatPostViews, UpdatePostView,DeletePostView
from django.urls import path

urlpatterns = [
    path('post/new',CreatPostViews.as_view(), name='create_post' ),
    path('',BlogPostViwes.as_view(), name='home'),
    path('post/<int:pk>/', FullPostViews.as_view(), name='full_post'),
    path('post/<int:pk>/edit', UpdatePostView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
]