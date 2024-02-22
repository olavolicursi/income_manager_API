from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        # Use make_password para criptografar a senha antes de salvar no banco de dados
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    
    def update(self, instance, validated_data):
        # Se a senha foi incluída na atualização, criptografe-a antes de salvar
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])

        return super(UserSerializer, self).update(instance, validated_data)