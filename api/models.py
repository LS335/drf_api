from django.db import models
import uuid

class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    topic = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chat = models.CharField(max_length=300)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="comments")


