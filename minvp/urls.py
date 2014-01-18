# Import from Django
from django.conf.urls import patterns, include, url
from django.contrib import admin

# Imports from this module (explicit relative imports)
from apps.home.views import HomePageView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'', HomePageView.as_view(), name='home_page'),
    url(r'^admin/', include(admin.site.urls)),
)