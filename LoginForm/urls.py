from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginView, name="login"),
    path('blog',views.blog, name="blog"),
    path('logout/',views.logoutView, name="logout")
]
