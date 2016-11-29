from films.models import *
from films.serializers import *
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pdb

class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get(self, request, *args, **kwargs):
        title = request.GET.get('title', '')
        year_prod = request.GET.get('year_prod', '')
        if year_prod == '':
            films = Film.objects.all()
        else:
            films = Film.objects.filter(year_prod=year_prod)
        if title == '':
            films = Film.objects.all()
        else:
            films = Film.objects.filter(title__istartswith=title)
        serialized_films = FilmSerializer(films, many=True)
        return Response(serialized_films.data)

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class TheaterList(generics.ListCreateAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

class TheaterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
