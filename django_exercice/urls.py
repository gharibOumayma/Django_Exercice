from django.conf.urls import include, url
from django.contrib import admin
from django_exercice import views as django_exercice_views
urlpatterns = [

    url(r'^$', django_exercice_views.login_redirect, name='login_redirect'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('django_exercice.profiles.urls')),

]
