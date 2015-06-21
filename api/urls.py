from django.conf.urls import url
from api import views

urlpatterns = [
    # url(r'^in/$', views.import_data, name='import_data'),
    url(r'^$', views.job, name='job'),
]
