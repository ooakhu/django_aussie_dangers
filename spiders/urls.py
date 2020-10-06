from django.urls import path
from .import views

urlpatterns = [
    path('', views.loginx,name='loginx'),
    path('<int:spider_id>', views.detail, name='detail'),

]