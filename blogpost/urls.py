from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.BlogpostListCreateAPIView.as_view(), name="Create/List posts"),
    path("posts/<int:pk>/", views.BlogPostDetailAPIView.as_view(), name="Get specific post/UpdateDelte by Author"),
    path("upload/image/", views.BlogimageCreateAPIViews.as_view(), name="Uploads image by Author"),
    path("update/image/<int:pk>/", views.BlogimageRetrieveUpdateDestroyAPIViews.as_view(), name="update/delete image by Author"),
]