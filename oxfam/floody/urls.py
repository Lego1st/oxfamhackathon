from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views
app_name = 'floody'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^accounts/registered/$', views.register_complete, name='register complete'),
    url(r'^accounts/loggedin/$', views.loggin_view, name='logged in'),
    url(r'^accounts/loggedout/$', views.logout_view, name='logged out'),
]
