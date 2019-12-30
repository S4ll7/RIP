from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from .blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.MainView.as_view(), name='main'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostView.as_view(), name='postDetail'),
    url(r'^registration/', views.RegistrationForm.as_view(), name='registration'),
    url(r'^login/', views.LoginForm.as_view(), name='login'),
    url(r'^profile/', views.user_profile, name='profile'),
    url(r'^logout/', views.LogoutForm.as_view(), name='logout'),
]
