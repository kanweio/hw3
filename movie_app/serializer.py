from rest_framework import serializers

from movie_app.models import Director, Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'stars', 'movie')


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'reviews', 'rating')

    def get_rating(self, movie):
        stars_list = [review.stars for review in movie.reviews.all()]
        return sum(stars_list) / max(1, len(stars_list))


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count')

    def get_movies_count(self, director):
        return director.movies.count()
