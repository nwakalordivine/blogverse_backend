from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.BlogpostListCreateAPIView.as_view(), name="Create/List posts"),
    path("posts/<int:pk>/", views.BlogPostDetailAPIView.as_view(), name="Get specific post/UpdateDelte by Author"),
    path("upload/image/", views.BlogimageCreateAPIViews.as_view(), name="Uploads image by Author"),
    path("update/image/<int:pk>/", views.BlogimageRetrieveUpdateDestroyAPIViews.as_view(), name="update/delete image by Author"),
    path('comments/', views.CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
    path('posts/?search=<search_term>', views.BlogpostListCreateAPIView.as_view(), name="search posts by title, tag or category"),
    path('posts/<int:pk>/like/', views.LikePostAPIView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', views.UnlikePostAPIView.as_view(), name='unlike-post'),
    path('posts/trending/', views.TrendingPostsAPIView.as_view(), name='trending-posts'),
    path('notifications/', views.NotificationListAPIView.as_view(), name='notifications'),
    path('dashboard/', views.AuthorDashboardAPIView.as_view(), name='author-dashboard')
]