from django.conf.urls import url

from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$',views.register_view, name='register_view'),
    url(r'^register/register/$',views.register,name='register'),
    url(r'^login/$',views.login,name='login'),
    url(r'^success/$',views.success,name='success')
]
