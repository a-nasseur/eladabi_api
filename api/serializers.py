from dataclasses import field
from rest_framework import serializers
from .models import Article
from .models import Category
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Article
        fields = ['id',  'title', 'slug', 'excerpt', 'featured', 'category',
                  'author', 'thumbnail', 'image', 'body', 'tags', 'created_date']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CommentSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    article = serializers.ReadOnlyField(source='article.id')

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'article', 'message', 'created_date']
