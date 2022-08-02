from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import Post, Like


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )

    @action(methods=['get'], detail=False)
    def likes_list(self, request):
        likes = Like.objects.all()
        return Response({'likes_ans': [like.id for like in likes]})

    @action(methods=['get'], detail=True)
    def current_like(self, request, pk=None):
        if pk:
            like = Like.objects.filter(id=pk)
            if like:
                return Response({'like_author': like.author_fk.id})
            return Response({'error': "like does not exist"})

    # for more difficult logic with queryset
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Post.objects.all()
        return Like.objects.filter(id=pk)
