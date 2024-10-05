from rest_framework import serializers
from .models import Project, Blog, Career, Comment

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        
class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at']