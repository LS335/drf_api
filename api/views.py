from django.shortcuts import render
from api.models import Board, Comment
from rest_framework import generics
from .serializers import BoardSerializer, CommentSerializer

class BoardListView(generics.ListCreateAPIView):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()

class BoardRetrieveView(generics.RetrieveDestroyAPIView):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        return Comment.objects.filter(board__pk=self.kwargs['board_pk'])

    def perform_create(self, serializer):
        super().perform_create(serializer)
        board = Board.objects.get(pk=self.kwargs['board_pk'])
        board.comments.add(serializer.instance)

class CommentRetrieveView(generics.RetrieveDestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(board__pk=self.kwargs['board_pk'])

