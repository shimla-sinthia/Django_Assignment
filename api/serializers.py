from rest_framework import serializers
from api.models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class DogSerializer(serializers.ModelSerializer):
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())

    class Meta:
        model = Dog
        fields = '__all__'

    def create(self, validated_data):
        breed = validated_data.pop('breed')
        breed_id = breed.id if isinstance(breed, Breed) else breed
        breed = Breed.objects.get(id=breed_id)
        dog = Dog.objects.create(breed=breed, **validated_data)
        return dog