from django.shortcuts import render

###########MODELS (TABLES) IMPORTS###################
from app.models import Reviewer, Movie, MovieReview

##############SERIALIZER IMPORTS################
from app.serializers import MovieSerializer

#########V1 FRAMEWORK IMPORTS######################
from rest_framework.views import APIView
from rest_framework.response import Response

############### Movies; Return Movies, Create New Movie ###########
class MovieListCreateAPIView(APIView):
    def get(self, request):
        all_movies = Movie.objects.all()
        serialized_movies = MovieSerializer(all_movies, many=True)
        return Response(serialized_movies.data, 200)


    def post(self, request):
        pass

#########################################
