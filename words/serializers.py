from rest_framework import serializers

from .models import Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = 'id', 'word', 'translation', 'description', 'repeated'

    def save(self, **kwargs):
        if self.partial:
            for k, v in self.validated_data.items():
                if getattr(self.instance, k) != v:
                    setattr(self.instance, k, v)

            self.instance.save()
            return self.instance

        data = self.validated_data
        data['user'] = self.context['request'].user
        instance = Word.objects.create(**data)
        return instance
