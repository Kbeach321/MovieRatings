from rest_framework import serializers
from app.models import Reviewer, MovieReview, Movie

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['title', 'imdb_link', 'director', 'year', 'genre']
        pass

class MovieReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieReview
        fields = ['stars']
        pass

class ReviewerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviewer
        fields = ['age', 'occupation', 'postal_code']
        pass
