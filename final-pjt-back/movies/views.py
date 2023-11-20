from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests, json
from django.conf import settings
from .serializers import MovieSerializer

# Create your views here.
TMDB_URL = 'https://api.themoviedb.org/3/'
TMDB_API_KEY = settings.TMDB_API_KEY

# api_key로 데이터 받아오기
@api_view(['GET'])
def getdata(request):
    movie_list = []
    for i in range(1, 2):
        url = f"{TMDB_URL}movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(url).json()

        for movie in movies['results']:
            if movie.get('release_date', '') and (movie.get('overview') != '' and movie.get('poster_path') != None and movie.get('release_date') != None):
                movie = {
                    'adult': movie['adult'],
                    'genres': movie['genre_ids'],
                    'id': movie['id'],
                    'overview': movie['overview'],
                    'popularity': movie['popularity'],
                    'poster_path': movie['poster_path'],
                    'release_date': movie['release_date'],
                    'title': movie['title'],
                    'vote_average': movie['vote_average'],
                    'vote_count': movie['vote_count'],
                    'movie_like_users': []
                }
                movie_list.append(movie)
                # serializer = MovieSerializer(movie)
                # print(serializer.data)
    # return Response(serializer.data)
    return Response(movie_list)