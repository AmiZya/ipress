from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging_autocomplete.models import TagAutocompleteField

class Category(models.Model):
    name = models.CharField(_('Category'), max_length=128, default='Uncategorized')

    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(_('article title'), max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(User)
    photo = models.ImageField(_('article photo'),upload_to='articles/photos/',blank=True,null=True)
    body = models.TextField(_('article body'))
    is_draft = models.BooleanField(default=True)
    category = models.ManyToManyField('Category')
    tags = TagAutocompleteField()
    created = models.DateTimeField(_('article created at'),auto_now_add=True)
    modified = models.DateTimeField(_('article modified at'),auto_now=True)


    def __unicode__(self):
        return '%s by: %s' %(self.title, self.author.username)


