from .models import Blogpost
from .serializers import BlogpostSerializer, BlogimageSerializer
from rest_framework import generics
from blogpost.permissions import IsOwnerOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
# Create your views here.

class BlogpostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerializer

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
    
class BlogimageCreateAPIViews(generics.CreateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogimageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    

class BlogimageRetrieveUpdateDestroyAPIViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogimageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'
