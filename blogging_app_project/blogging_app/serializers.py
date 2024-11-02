from .models import User, Category, Post, Comment, Like
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = "__all__" # all fields name
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = "__all__" # all fields name
  
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Post
        fields = "__all__" # all fields name
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Comment
        fields = "__all__" # all fields name
   
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Like
        fields = "__all__" # all fields name
    


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)