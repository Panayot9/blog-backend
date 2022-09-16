import datetime
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

        start_date = self.request.query_params.get('start_date')
        if start_date is not None:
            queryset = queryset.filter(created_at__gte=datetime.datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')).distinct()

        end_date = self.request.query_params.get('end_date')
        if end_date is not None:
            queryset = queryset.filter(created_at__lte=datetime.datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')).distinct()

        return queryset
