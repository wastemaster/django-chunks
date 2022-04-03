from modeltranslation.translator import translator, TranslationOptions

from . import models


class ChunkOpts(TranslationOptions):
    fields = ('content', )
translator.register(models.Chunk, ChunkOpts)


class ChunkGroupOpts(TranslationOptions):
    fields = ('content', )
translator.register(models.Group, ChunkGroupOpts)


class ChunkMediaOpts(TranslationOptions):
    fields = ('title', 'desc', 'media', )
translator.register(models.Media, ChunkMediaOpts)
