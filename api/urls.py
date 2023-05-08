from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.getRoutes),
    path('data/',views.getData),
    path('data/<int:pk>/',views.getDatabyID),
    path('data/topic/<str:pk>/', views.getDatabyTopic),

]
