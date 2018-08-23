from django.apps import AppConfig
from django.conf import settings
from elasticsearch_dsl.connections import connections

class ElasticsearchappConfig(AppConfig):
    name = 'emails'

    def ready(self):
        connections.configure(**settings.ELASTICSEARCH)