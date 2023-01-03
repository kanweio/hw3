from django.contrib import admin

# Register your models here.
from django.contrib import admin
from movie_app.models import Director, Movie, Review


# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "reviews")
    list_display_links = ("title",)
    search_fields = ("title", "description")


admin.site.register(Director)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
