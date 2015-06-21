from django.conf.urls import include, url
from django.contrib import admin
from elzup_api import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'elzup_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.job, name='job'),
]
