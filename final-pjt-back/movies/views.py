from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests, json
from django.conf import settings
from .models import Movie, Moviecomment
from .serializers import MovieSerializer, MovieDetailSerializer, CommentSerializer, GenreSerializer

# Create your views here.
TMDB_URL = 'https://api.themoviedb.org/3/'
TMDB_API_KEY = settings.TMDB_API_KEY

# api_key로 데이터 받아오기
@api_view(['GET'])
def getMovies(request):
    movie_list = []
    for i in range(1, 300):
        url = f"{TMDB_URL}movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(url).json()

        for movie in movies['results']:
            if movie.get('release_date', '') and (movie.get('overview') != '' and movie.get('poster_path') != None and movie.get('release_date') != None):
                fields = {
                    'adult': movie['adult'],
                    'genres': movie['genre_ids'],
                    'overview': movie['overview'],
                    'popularity': movie['popularity'],
                    'poster_path': movie['poster_path'],
                    'release_date': movie['release_date'],
                    'title': movie['title'],
                    'vote_average': movie['vote_average'],
                    'vote_count': movie['vote_count'],
                    'movie_like_users': []
                }
                movie = {
                    'model': 'movies.Movie',
                    'pk': movie['id'],
                    'fields': fields
                }

    #             movie_list.append(movie)
    #             serializer = MovieSerializer(data=movie)
    #             if serializer.is_valid(raise_exception=True):
    #                 serializer.save()
    # return Response(serializer.data)

    with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(movie_list, w, indent=4, ensure_ascii=False)

    return Response(movie_list)


@api_view(['GET'])
def getGenres(request):
    url = f"{TMDB_URL}genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
    genres = requests.get(url).json()
    genre_list = []
    for genre in genres['genres']:
        fields = {
            'name':genre['name']
        }

        genre = {
            'model': 'movies.Genre',
            'pk': genre['id'],
            'fields': fields
        }
        genre_list.append(genre)

    #     serializer = GenreSerializer(data=genre)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    # return Response(serializer.data, status=status.HTTP_200_OK)
    with open("movies/fixtures/movie_genre.json", "w", encoding="utf-8") as w:
        json.dump(genre_list, w, indent=4, ensure_ascii=False)

    return Response(genre_list)


# 전체 movie 정보 받아오기
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 영화 상세정보 받아오기
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


# 영화 전체 댓글 조회
@api_view(['GET'])
def comment_list(request):
    comments = Moviecomment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


# 영화 댓글 생성
@api_view(['POST'])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 영화 상세정보에서 댓글 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Moviecomment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

# 영화 좋아요(찜목록)
@api_view(['POST'])
def likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.movie_like_users.filter(pk=request.user.pk).exists():
        movie.movie_like_users.remove(request.user)
    else:
        movie.movie_like_users.add(request.user)
    return Response(status=status.HTTP_200_OK)
