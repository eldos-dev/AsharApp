from django.db.models import Avg
from rest_framework import serializers

from comment.models import Comment, Rating


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'suggestion')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['rating'] = instance.ratings.aggregate(Avg('rating'))
        return representation



class RatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга"""

    class Meta:
        model = Rating
        fields = ('id', 'rating', 'comment')

    def create(self, validated_data):
        request = self.context.get('request')
        rating = Rating.objects.create(author=request.user, **validated_data)
        return rating










# class CommentListSerializer(serializers.ModelSerializer):
#     """Вывод комментариев"""
#     class Meta:
#         list_serializer_class = FilterCommentListSerializer
#         model = Comment
#         fields = ("id", "text", "author", "suggestion")
