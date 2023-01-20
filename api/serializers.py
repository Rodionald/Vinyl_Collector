from rest_framework import serializers
from django.contrib.auth.models import User
from vinylcollector.models import Vinyl


class VinylSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Vinyl
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
