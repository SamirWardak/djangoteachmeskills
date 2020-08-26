from rest_framework import serializers
from .models import News


class ContactFormSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    email = serializers.EmailField()
    message = serializers.CharField()

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = (
            'id',
            'name',
            'create_date',
            'comment',
            'image',
            'file'
        )
        depth = 1