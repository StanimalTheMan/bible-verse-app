from django.contrib import admin
from .models import Verse, Comment

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment 

class VerseAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Verse, VerseAdmin)
admin.site.register(Comment)