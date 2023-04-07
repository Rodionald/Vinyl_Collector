from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from vinylcollector.models import Vinyl, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'],
                                       name=validated_data['name']
                                       )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.title = profile_data.get('title', profile.title)
        profile.dob = profile_data.get('dob', profile.dob)
        profile.address = profile_data.get('address', profile.address)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.zip = profile_data.get('zip', profile.zip)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance


class VinylSerializer(serializers.ModelSerializer):
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
