from django.contrib import admin

# Register your models here.

from .models import Question, User, Choice, Listing

admin.site.register([Question, User, Choice, Listing])