import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Note(models.Model):
    """ Model containing data for each note """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=100, default=None)

    def __unicode__(self):
        return self.title


class NoteItem(models.Model):
    """ Corresponds to one item in a Note."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='items')
    text = models.CharField(max_length=100, default=None)