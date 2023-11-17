from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings

# Create your views here.

# api_key로 데이터 받아오기
def getdata(request):
    url = "https://api.themoviedb.org/3/movie/popular?api_key=4c5ad12762391c65cbb04605be859ce5&language=ko-KR&page=1"
    response = requests.get(url).json()
    print(response)
    return response
