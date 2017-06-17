from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets

# MODEL IMPORTS
from project.notes.models import Note, NoteItem

# SERIALIZER IMPORTS
from project.notes.serializers import UserSerializer, NoteSerializer, NoteItemSerializer


def board(request):
    user = request.user
    template_name = 'notes/board.html'
    return render(request, template_name, locals())


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows note items to be viewed or edited.
    """
    queryset = NoteItem.objects.all()
    serializer_class = NoteItemSerializer
