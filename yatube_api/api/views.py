from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)

from posts.models import Follow, Group, Post
from .permissions import ReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, ReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, ReadOnly)

    def get_post(self):
        post = get_object_or_404(
            Post,
            id=self.kwargs.get('post_id')
        )
        return post

    def get_queryset(self):
        post = self.get_post()
        return post.comments

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    # print(kwargs)
    # queryset = Follow.objects.get()
    # queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following',)

    def get_queryset(self):
        print(self.request.user)
        return Follow.objects.all().filter(user=self.request.user)
