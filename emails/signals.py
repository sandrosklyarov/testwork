from emails.models import EMailPost
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=EMailPost)
def index_post(instance, **kwargs):
    instance.indexing()