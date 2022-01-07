from django.contrib import admin
from .models import News, Message, Comment
# Register your models here.

admin.site.register(News)
admin.site.register(Message)
admin.site.register(Comment)