from .models import Note
from .serializers import NoteSerializer

class NoteCRUDMixin():
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
