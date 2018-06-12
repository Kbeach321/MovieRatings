from django.shortcuts import render

###########MODELS (TABLES) IMPORTS###################
from app.models import Reviewer, Movie, MovieReview

##############SERIALIZER IMPORTS################
from app.serializers import MovieSerializer, ReviewerSerializer, MovieReviewSerializer

#########V1 FRAMEWORK IMPORTS######################
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

############### Movies; Return Movies, Create New Movie ###########
class MovieListCreateAPIView(APIView):
    def get(self, request):
        all_movies = Movie.objects.all()
        serialized_movies = MovieSerializer(all_movies, many=True)
        return Response(serialized_movies.data, 200)


    def post(self, request):
        title = request.POST['title']
        imdb_link = request.POST['imdb_link']
        director = request.POST['director']
        year = request.POST['year']
        genre = request.POST['genre']
        new_movie = Movie.objects.create(title=title, imdb_link=imdb_link, director=director, year=year, genre=genre)
        serialized_new_movie = MovieSerializer(new_movie)
        return(serialized_new_movie.data, 201)

############## Movie; Return a SINGLE movie, edit, Delte #################

class MovieDetailAPIView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        serialized_movie = MovieSerializer(movie)
        return Response(serialized_movie.data, 200)

    def put(self, request, pk):
        movie = Movie.objects.get(id=pk)
        movie.title = request.POST['title']
        movie.imdb_link = request.POST['imdb_link']
        movie.director = request.POST['director']
        movie.year = request.POST['year']
        movie.genre = request.POST['genre']
        move.save()
        serialized_movie = MovieSerializer(movie)
        return(serialized_movie.data, 201)

    def delete(self, request, pk):
        movie = Movie.objects.get(id=pk)
        movie.delete()
        return Response("", 204)

################# Reviewer; Return Reviewers, Create New Reviewer #############

class ReviewerListCreateAPIView(APIView):
    def get(self, request):
        all_reviewers = Reviewer.objects.all()
        serialized_reviewers = ReviewerSerializer(all_reviewers, many=True)
        return Response(serialized_reviewers.data, 200)

    def post(self, request):
        age = request.POST['age']
        occupation = request.POST['occupation']
        postal_code = request.POST['postal_code']
        new_reviewer = Reviewer.objects.create(age=age, occupation=occupation, postal_code=postal_code)
        serialized_new_reviewer = ReviewerSerializer(new_reviewer)
        return(serialized_new_reviewer.data, 201)

########### Reviewer; Return a single reviewer, edit, delete ################

class ReviewerDetailAPIView(APIView):
    def get(self, request, pk):
        reviewer = Reviewer.objects.get(id=pk)
        serialized_reviewer = ReviewerSerializer(reviewer)
        return Response(serialized_reviewer.data, 200)

    def put(self, request, pk):
        reviewer = Reviewer.objects.get(id=pk)
        reviewer.age = request.POST['age']
        reviewer.occupation = request.POST['occupation']
        reviewer.postal_code = request.POST['postal_code']
        reviewer.save()
        serialized_reviewer = ReviewerSerializer(reviewer)
        return Response(serialized_reviewer.data, 201)

    def delete(self, request, pk):
        reviewer = Reviewer.objects.get(id=pk)
        reviewer.delete()
        return Response("", 204)

################## MovieReview, return list, create new ###############

class MovieReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer

################### Moviereview; SINGLE Return, Update, Delete ####################

class MovieReviewRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer
