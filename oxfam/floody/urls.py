from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views
app_name = 'floody'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^post/$', views.postimage, name='userpost'),

]
