from django.contrib.auth.models import User
from rest_framework import serializers

# MODEL IMPORTS
from project.notes.models import Note, NoteItem


class UserSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='note-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'notes')


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='noteitem-detail')

    class Meta:
        model = Note
        fields = ('id', 'owner', 'title', 'items')


class NoteItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = NoteItem
        fields = ('id', 'note', 'text')
