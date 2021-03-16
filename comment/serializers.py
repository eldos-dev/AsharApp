from rest_framework import serializers

from comment.models import Comment


class FilterCommentListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    """Добавление коммента"""

    class Meta:
        model = Comment
        fields = ('id', 'text', 'suggestion')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment


class CommentListSerializer(serializers.ModelSerializer):
    """Вывод комментариев"""
    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id", "text", "author", "suggestion")
