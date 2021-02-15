from django.contrib import admin
from django.urls import path
from boards import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', accounts_views.signup, name='signup'),
    path('boards/<pk>/', views.board_topics, name='board_topics'),
    path('boards/<pk>/new/', views.new_topic, name='new_topic'),
]
