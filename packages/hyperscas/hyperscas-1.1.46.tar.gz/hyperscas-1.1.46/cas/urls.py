from django.conf.urls import url

from . import views

app_name = 'cas'

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'users/(?P<pk>\w+)/language', views.language, name='language')
]
