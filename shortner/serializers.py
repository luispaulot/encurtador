from rest_framework import serializers
from rest_framework.views import Response
from .models import Url



def validate_url_hash(data):
    if Url.objects.filter(url_hash=data).exists():
        raise serializers.ValidationError("Essa url curta não está disponível no momento, informe outra ou deixe comigo :)")


class UrlSerializer(serializers.ModelSerializer):
    url_full = serializers.CharField()
    url_hash = serializers.CharField(required=False, allow_blank=True, validators=[validate_url_hash])
    expired_at = serializers.DateTimeField(required=False, format="%d-%m-%Y %H:%M")
    
    class Meta:
        model = Url
        fields = '__all__'
        
