from django.contrib import admin
from django.urls import path
from boards import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('boards/<pk>/', views.board_topics, name='board_topics'),
]
