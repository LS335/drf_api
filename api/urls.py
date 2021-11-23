from django.urls import path
from .views import BoardListView, BoardRetrieveView, CommentListView, CommentRetrieveView


urlpatterns = [
    path('boards/', BoardListView.as_view()),
    path('boards/<pk>/', BoardRetrieveView.as_view()),
    path('boards/<board_pk>/comments/', CommentListView.as_view()),
    path('boards/<board_pk>/comments/<pk>/', CommentRetrieveView.as_view()),
]