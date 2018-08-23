# -*- coding: utf-8 -*-

import emails.views
from django.urls import path

app_name = 'emails'

urlpatterns = [
    path('', emails.views.email_view, name='emails_search'),
    path('zip/', emails.views.zip_ajax, name='zip_ajax')
]