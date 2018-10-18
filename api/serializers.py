from rest_framework import serializers
from .models import Note, Student


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'name', 'body')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'year_in_school', 'level_class', 'phone_number')
