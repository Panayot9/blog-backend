from django.urls import path

from .views import PostList, PostDetail, SearchResultsListView, UserList, UserDetail

urlpatterns = [
    path("users/", UserList.as_view(), name='users_list'),
    path("users/<int:pk>/", UserDetail.as_view(), name='user_detail'),
    path('', PostList.as_view(), name='posts_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path("search/", SearchResultsListView.as_view(), name="search"),
]
