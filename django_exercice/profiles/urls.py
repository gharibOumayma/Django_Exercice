from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout
from django_exercice.profiles.forms import LoginForm

urlpatterns = [

    url(r'^profile/$', views.profile , name='profile'),
    url(r'^login/$', login, {'template_name': 'profiles/login.html', 'authentication_form': LoginForm}),
    url(r'^register/$', views.register , name='register'),
    url(r'^logout/$', logout,  {'next_page': '/login'}),

]
