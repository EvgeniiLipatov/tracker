from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, user_activate_view, UserChangeView, UserChangePasswordView, \
    UserDetailView, UserListView

app_name = 'accounts'

urlpatterns = [
#path('login/', login_view, name='login'),
#path('logout/', logout_view, name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('activate/<token>/', user_activate_view, name='user_activate'),
    path('profile/<pk>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/<pk>/edit/', UserChangeView.as_view(), name='user_update'),
    path('profile/<pk>/change-password/', UserChangePasswordView.as_view(), name='user_change_password'),
    path('listuser/', UserListView.as_view(), name='user_list')
]