from rest_framework import serializers
from rest_app.models import RestElements

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestElements
        fields = 'id', 'rest_text', 'sent'