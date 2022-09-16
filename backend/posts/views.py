from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django.views.generic import ListView

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class SearchResultsListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        username = self.request.user.username
        queryset = Post.objects.filter(author__username=username)
        q = self.request.query_params.get('q')
        if q is not None:
            queryset = queryset.filter(title__icontains=q).distinct()

        return queryset
