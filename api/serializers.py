from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from vinylcollector.models import Vinyl


class VinylSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Vinyl
        fields = '__all__'

        @staticmethod
        def create(validated_data):
            return Vinyl.objects.create(**validated_data)

        @staticmethod
        def update(instance, validated_data):
            instance.artist = validated_data.get('artist', instance.artist)
            instance.album = validated_data.get('album', instance.album)
            instance.genres = validated_data.get('genres', instance.genres)
            instance.styles = validated_data.get('styles', instance.styles)
            instance.notes = validated_data.get('notes', instance.notes)
            instance.formats = validated_data.get('formats', instance.formats)
            instance.qty = validated_data.get('qty', instance.qty)
            instance.manufacture_region = validated_data.get('manufacture_region', instance.manufacture_region)
            instance.label = validated_data.get('label', instance.label)
            instance.year = validated_data.get('year', instance.year)
            instance.image_url = validated_data.get('image_url', instance.image_url)
            instance.save()
            return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'first_name', 'is_active']

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    @staticmethod
    def get_token(user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
