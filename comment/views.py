from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListCreateAPIView

from comment.models import Comment, Rating
from comment.serializers import CommentSerializer, RatingSerializer
from term.permissions import IsAuthorPermission


class CommentCreateView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Comment.objects.select_related('author', 'suggestion')
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CommentListView(ListAPIView):
    queryset = Comment.objects.select_related('author', 'suggestion')
    serializer_class = CommentSerializer


class CommentDetailView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorPermission, )


class RatingListCreateView(ListCreateAPIView):
    queryset = Rating.objects.select_related('author', 'comment')
    serializer_class = RatingSerializer
    permission_classes = (permissions.IsAuthenticated, )
