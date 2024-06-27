from django.urls import path
from meetings import views

urlpatterns = [
    path('<int:id>/', views.detail, name="detail"),
    path('rooms', views.roomdirectory, name="roomdirectory"),
    path('create/', views.create, name="create"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete"),
]