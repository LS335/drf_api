from rest_framework import serializers
from .models import Board, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'chat', 'board']


class BoardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)


    class Meta:
        model = Board
        fields = ['id', 'title', 'topic', 'comments']