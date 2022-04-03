from django.contrib import admin

from . import models


@admin.register(models.Chunk)
class ChunkAdmin(admin.ModelAdmin):
    list_display = ('key', 'content')
    search_fields = ('key', 'content')


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('key', 'content')
    list_filter = ('key', )
    search_fields = ('key', 'content')


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('key', )
    search_fields = ('key', )


@admin.register(models.Media, MediaAdmin)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('key', 'title')
    search_fields = ('key', 'title', 'desc')
