from django.contrib import admin
from django.urls import path
from boards import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('boards/<pk>/', views.board_topics, name='board_topics'),
    path('boards/<pk>/new/', views.new_topic, name='new_topic'),
]
