from django.conf.urls import url
from django.contrib.auth import views as auth_views

from. import views

urlpatterns = [
    url (r'^$', views.index, name = 'index'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name= 'login.html', redirect_authenticated_user=True ), name ='login'),
    url(r'^Logout/$', auth_views.LogoutView.as_view(), name = 'logout'),
    url (r'^entro/$', views.entro, name = 'entro'),
    url (r'^perfil/$', views.perfil, name = 'perfil'),
]
