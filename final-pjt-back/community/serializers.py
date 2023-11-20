from rest_framework import serializers
from .models import Article, Articlecomment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content',)
        read_only_fields = ('user',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articlecomment
        fields = '__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):
    articlecomment_set = CommentSerializer(many=True, read_only=True)    

    class Meta:
        model = Article
        fields = '__all__'