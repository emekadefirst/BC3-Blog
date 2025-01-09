from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content']


admin.site.register(Note, NoteAdmin)
