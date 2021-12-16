from django.urls import path
from .import views

app_name = 'esearch'
urlpatterns = [
    # path('',views.suggest_result,name='suggest_result'),
    path('', views.search_result, name='search_result'),
    path('about/', views.about, name='about'),
]
