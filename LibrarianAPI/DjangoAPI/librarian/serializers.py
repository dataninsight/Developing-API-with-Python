from rest_framework import serializers
from .models import Librarian

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = ['id', 'title', 'content']
