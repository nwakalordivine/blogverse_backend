from .models import Blogpost, Comment, Notification
from .serializers import BlogpostSerializer, BlogimageSerializer, CommentSerializer, NotificationSerializer, AuthorDashboardSerializer
from rest_framework import generics, permissions, filters
from blogpost.permissions import IsOwnerOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from core.models import Userprofile
from django.shortcuts import get_object_or_404
# Create your views here.

class BlogpostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'tags', 'category']

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return[AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class BlogPostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
    

class BlogimageUpdateAPIViews(generics.UpdateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogimageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'



class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsOwnerOrReadOnly()]
        return [permissions.AllowAny()]

class ToggleLikePostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Blogpost.objects.get(pk=pk)
        user = request.user
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            status = 'unliked'
        else:
            post.likes.add(user)
            status = 'liked'
            # Send notification only on like
            if post.author != user:
                Notification.objects.create(
                    recipient=post.author,
                    sender=user,
                    post=post,
                    notification_type='like',
                    message=f"{user.userprofile.first_name} liked your post."
                )
        return Response({'status': status, 'like_count': post.like_count})

class TrendingPostsAPIView(generics.ListAPIView):
    serializer_class = BlogpostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Blogpost.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')

class NotificationListAPIView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')

class AuthorDashboardAPIView(generics.GenericAPIView):
    serializer_class = AuthorDashboardSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        profile = Userprofile.objects.get(user=user)
        posts = Blogpost.objects.filter(author=user)
        total_likes = sum(post.likes.count() for post in posts)

        dashboard_data = {
            "first_name": profile.first_name,
            "last_name": profile.last_name,
            "avatar": profile.avatar.url if profile.avatar else None,
            "total_likes": total_likes,
            "posts": posts  # <-- Pass queryset, not serialized data!
        }
        serializer = self.get_serializer(dashboard_data, context={'request': request})
        return Response(serializer.data)

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = get_object_or_404(Blogpost, pk=self.kwargs['pk'])
        comment = serializer.save(author=self.request.user, post=post)
        
        # Send notification
        if post.author != self.request.user:
            Notification.objects.create(
                recipient=post.author,
                sender=self.request.user,
                post=post,
                notification_type='comment',
                message=f"{self.request.user.userprofile.first_name} commented on your post."
            )

