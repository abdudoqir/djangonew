from django.urls import path

from pools import views

app_name = 'pools'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
