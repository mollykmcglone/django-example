from rest_framework import serializers
from films.models import *

class FilmSerializer(serializers.ModelSerializer):
	genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), allow_null=True)

	class Meta:
		model = Film
		fields = ('id', 'title', 'year_prod', 'genre')

class TheaterSerializer(serializers.ModelSerializer):
	films = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all(), allow_null=True)

	class Meta:
		model = Theater
		fields = ('id', 'name', 'city', 'state', 'films')

class GenreSerializer(serializers.ModelSerializer):

	class Meta:
		model = Genre
		fields = ('id', 'name')
