from django.db import models

############### Reviewer Class ####################
class Reviewer(models.Model):
    age = models.CharField(max_length=3)
    occupation = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=12)

################ Movie Class ####################
class Movie(models.Model):
    title = models.CharField(max_length=255)
    imdb_link = models.URLField(max_length=500)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)

############ MovieReview Class #####################
class MovieReview(models.Model):
    stars = models.IntegerField()

        ######### ForeignKeys #########
    reviewer = models.ForeignKey(Reviewer, null=True, on_delete=models.SET_NULL)
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL)
