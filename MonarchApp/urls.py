from django.urls import path
from . import views


urlpatterns = [
    path('api/login',views.user_login),

]