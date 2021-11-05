from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=20)
    image = serializers.CharField(max_length=100)
    likes = serializers.IntegerField(default=0)
    owner = serializers.ReadOnlyField(source='owner.username')


    def create(self, validated_data):
        return Products.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.save()
        return instance

    class Meta:
        model = Products
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Products.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'products')
        extra_kwargs = {'password': {'write_only': True}}

