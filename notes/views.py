from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     CreateAPIView,
                                     DestroyAPIView)
from .models import Note
from .serializers import NoteSerializer
from .mixins import NoteCRUDMixin

# Create your views here.

class NoteListCreateAPIView(NoteCRUDMixin,
                            ListCreateAPIView):
    queryset = Note.objects.all().order_by('-updated')
    pass

note_list_create_view = NoteListCreateAPIView.as_view()


class NoteRetrieveAPIView(NoteCRUDMixin,
                          RetrieveAPIView):
    pass

note_retrieve_view = NoteRetrieveAPIView.as_view()

class NoteUpdateAPIView(NoteCRUDMixin,
                        UpdateAPIView):
    pass

note_update_view = NoteUpdateAPIView.as_view()

class NoteCreateAPIView(NoteCRUDMixin,
                          CreateAPIView):
    pass

note_create_view = NoteCreateAPIView.as_view()

class NoteDeleteAPIView(NoteCRUDMixin,
                          DestroyAPIView):
    pass

note_delete_view = NoteDeleteAPIView.as_view()