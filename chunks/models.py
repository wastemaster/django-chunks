from django.core.cache import cache
from django.db import models
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

from . import managers

CACHE_PREFIX = 'chunks_'


class BaseChunk(models.Model):

    key = models.CharField(_('key'), max_length=255, unique=True,
                           help_text=_('A unique name for this chunk of content'))

    content_type = 'unknown'

    class Meta:
        abstract = True
        ordering = ('key', )

    def __unicode__(self):
        return self.key

    def save(self, *args, **kwargs):
        cache_key = CACHE_PREFIX + self.content_type + get_language() + self.key
        cache.delete(cache_key)  # cache invalidation on save
        super(BaseChunk, self).save(*args, **kwargs)


class Chunk(BaseChunk):
    """
    A Chunk is a piece of content associated
    with a unique key that can be inserted into
    any template with the use of a special template
    tag
    """
    content = models.TextField(_('content'), blank=True)

    content_type = 'text'

    class Meta(BaseChunk.Meta):
        verbose_name = _('Text Chunk')
        verbose_name_plural = _('Text Chunks')


class Group(models.Model):
    u"""
    A Group is a list of content associated
    with a unique key that can be inserted into
    any template with the use of a special template
    tag
    """
    key = models.CharField(_('key'), max_length=255, unique=False,
                           help_text=_('A name for chunks group'))
    content = models.TextField(_('content'), blank=True)

    content_type = 'group'

    class Meta:
        verbose_name = _('Group Chunk')
        verbose_name_plural = _('Group Chunks')
        ordering = ('key', )

    def __unicode__(self):
        return self.key

    def save(self, *args, **kwargs):
        cache_key = CACHE_PREFIX + self.content_type + get_language() + self.key
        cache.delete(cache_key)  # cache invalidation on save
        super(Group, self).save(*args, **kwargs)


class Image(BaseChunk):
    """
    The same thing like Chunk but for images.
    """
    image = models.ImageField(_('image'), upload_to='chunks/images', max_length=255)

    content_type = 'text'

    objects = managers.ImageManager()

    class Meta(BaseChunk.Meta):
        verbose_name = _('Image Chunk')
        verbose_name_plural = _('Image Chunks')


class Media(BaseChunk):
    """
    The same thing like Chunk but for files.
    """
    title = models.CharField(max_length=64, verbose_name=_('Title'))
    desc = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('Description'))
    media = models.FileField(upload_to='chunks/media', max_length=256, blank=True, null=True, verbose_name=_('Media'))

    content_type = 'text'

    class Meta(BaseChunk.Meta):
        verbose_name = _('Media Chunk')
        verbose_name_plural = _('Media Chunks')

    @staticmethod
    def get(key):
        cache_key = CACHE_PREFIX + 'media' + get_language() + key
        obj = cache.get(cache_key)
        if obj is None:
            obj, created = Media.objects.get_or_create(
                key=key, defaults={'title': key})
            cache.set(cache_key, obj)
        return obj
