from django.contrib import admin
from .models import Actor, Director, Writer, Genre, Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = ('title','director')
    list_filter = ('director','released')

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Writer)
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
