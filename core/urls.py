from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenBlacklistView, TokenObtainPairView
)
from django.urls import path
from . import views

urlpatterns = [
    # ...your existing endpoints...
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),      
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),           
    path('api/auth/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),            
    path('api/auth/register/', views.RegisterAPIView.as_view(), name='auth_register'),
    path("api/users/me/", views.UserMeAPIView.as_view(), name="user-me"),
    path("api/users/<int:pk>/", views.UserprofileDetailAPIView.as_view(), name="user-profile"),
    path("api/users/avatar/", views.AvatarUpdateAPIViews.as_view(), name="update-avatar"),
    path("api/admin/all-profile/", views.UserProfileListAPIView.as_view(), name="user-profile-list"),
    path("api/admin/userprofile/<int:pk>/update/", views.UserProfileRetrieveUpdateDeleteAPIView.as_view(), name="user-profile-update-delete"),
]
