from django.urls import path, include
from django.contrib import admin
import emails.urls

# admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emails/', include(emails.urls)),
]