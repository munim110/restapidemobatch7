from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Author, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(ModelSerializer):
    # author = serializers.SerializerMethodField()
    # easy_access = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'
        depth = 2

    # def get_author(self, obj):
    #     return {
    #         "name" : obj.author.name,
    #         "bio" : obj.author.bio,
    #     }
    # def get_easy_access(self,obj):
    #     return int(obj.price) <= 500