from django.contrib import admin

# Register your models here.
from .models import Book
admin.site.register(Book)

from .models import Book, Entry
admin.site.register(Entry)
