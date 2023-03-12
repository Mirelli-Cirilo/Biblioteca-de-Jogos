from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.gameList, name='game-list'),

    path('create_game/', views.createGame, name='create-game'),
    path('update_game/<str:pk>/', views.updateGame, name='update-game'),
    path('delete_game/<str:pk>/', views.deleteGame, name='delete-game'),
    path('detalhe_game/<str:pk>/', views.detalheGame, name='detalhe-game'),
    
]