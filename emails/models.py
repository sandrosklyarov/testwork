# -*- coding: utf-8 -*-
from django.db import models

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

class Tag(models.Model):
    text = models.CharField(max_length=1000)
    moderated = models.BooleanField(default=True)