from rest_framework import serializers
from .models import Movie, Genre, Moviecomment

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields='__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields= '__all__'


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Moviecomment
        fields = '__all__'
        read_only_fields = ('user', 'movie',)


class MovieDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    moviecomment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'