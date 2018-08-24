# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class EMailPost(models.Model):
    class Meta:
        app_label = 'emails'
    description = models.CharField(verbose_name=u'Тема письма', max_length=1000)
    text = models.TextField(u'Текст письма')
    created = models.DateTimeField()
    sender = models.CharField(verbose_name=u'Отправитель', max_length=1000)

    def __unicode__(self):
        return self.description

    def indexing(self):
        from emails.search import EmailIndex
        obj = EmailIndex(
            meta={'id': self.id},
            description=self.description,
            created=self.created,
            sender=self.sender,
            text=self.text
        )
        obj.save()
        return obj.to_dict(include_meta=True)

@receiver(post_save, sender=EMailPost)
def index_post(instance, **kwargs):
    instance.indexing()    
    
class Tag(models.Model):
    text = models.CharField(max_length=1000)
    moderated = models.BooleanField(default=True)
