from django.contrib import admin
from .models import Book, Author

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    # add filter to books on django admin
    list_filter = ('author', 'rating')
    # how to display books on django admin
    list_display = ('title','author')

admin.site.register(Book, BookAdmin)
admin.site.register(Author)