from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from accounts.views import showzippy
from accounts.views import status

from django.contrib import admin

# admin.autodiscover()

urlpatterns = [
    url(r"^zipcode/", showzippy),
    url(r"^status/", status),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
