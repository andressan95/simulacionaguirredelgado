from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.promedio_movil, name='promedio_movil')
]
