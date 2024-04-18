from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignUpView, UserLoginView, UserLogoutView

# urls.py
app_name = 'user'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]