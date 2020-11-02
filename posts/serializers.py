from rest_framework import serializers
from posts.models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerialize):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author']

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('title', instance.content)
        instance.author = validated_data.get('title', instance.author)
        instance.save()
        return instance