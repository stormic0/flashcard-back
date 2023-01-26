from random import choice

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from .serializers import WordSerializer
from .models import Word


class CreateWordAPIView(generics.CreateAPIView):
    serializer_class = WordSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        user = self.request.user
        queryset = Word.objects.filter(user=user)
        return queryset


class RetrieveWordAPIView(generics.RetrieveAPIView):
    serializer_class = WordSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        user = self.request.user
        repeated_number = self.request.query_params.get('repeated')
        queryset = Word.objects.filter(user=user, repeated__lte=int(repeated_number)) if repeated_number else Word.objects.filter(user=user)
        return queryset

    def get_object(self):
        qs = self.get_queryset()
        if not qs:
            raise ValidationError('"message": "No Word Found!"\n"status": "404 - Not Found"')

        obj = choice(qs)
        obj.add_repeat()
        return obj


class UpdateWordAPIView(generics.UpdateAPIView):
    serializer_class = WordSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        user = self.request.user
        queryset = Word.objects.filter(user=user)
        return queryset
