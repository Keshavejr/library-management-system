from collections.abc import Collection

from django.contrib import admin
from .models import Reader, Book, Collection


# Register your models here.
admin.site.register(Reader)
admin.site.register(Book)
admin.site.register(Collection)