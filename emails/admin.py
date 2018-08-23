from django.contrib import admin
from emails.models import EMailPost, Tag

# Register your models here.
admin.site.register(EMailPost)
admin.site.register(Tag)