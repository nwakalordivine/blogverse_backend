from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.BlogpostListCreateAPIView.as_view(), name="Create/List posts"),
    path("posts/<int:pk>/", views.BlogPostDetailAPIView.as_view(), name="Get specific post/UpdateDelte by Author"),
    path("update/image/<int:pk>/", views.BlogimageUpdateAPIViews.as_view(), name="update/delete image by Author"),
    path('comments/<int:pk>/upload/', views.CommentCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
    path('like/<int:pk>/', views.ToggleLikePostAPIView.as_view(), name='like-post'),
    path('trending/', views.TrendingPostsAPIView.as_view(), name='trending-posts'),
    path('notifications/', views.NotificationListAPIView.as_view(), name='notifications'),
    path('dashboard/', views.AuthorDashboardAPIView.as_view(), name='author-dashboard'),
    path('notifications/<int:pk>/', views.MarkNotificationAsReadAPIView.as_view(), name='mark-notification-as-read'),
    path('notifications/mark-all-read/', views.MarkAllNotificationsAsReadAPIView.as_view(), name='mark-all-notifications-as-read'),
    path('admin/posts/<int:pk>/', views.BlogpostRetrieveUpdateDestroyAPIView.as_view(), name='admin-post-detail'),
    path('admin/comments/<int:pk>/', views.AdminCommentRetrieveUpdateDestroyAPIView.as_view(), name='admin-comment-detail'),
]