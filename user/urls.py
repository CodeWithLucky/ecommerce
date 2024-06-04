from django.urls import path
from . import admin
from .views import (
    UserListView,
    login_view,signup_view
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    # path('user/<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
    # path('user/create/', UserCreateView.as_view(), name='user_create'),
    # path('user/update/<int:user_id>/', UserUpdateView.as_view(), name='user_update'),
    # path('user/delete/<int:user_id>/', UserDeleteView.as_view(), name='user_delete'),
    # path('accounts/', AccountListView.as_view(), name='account_list'),
    # path('roles/', RoleListView.as_view(), name='role_list'),
    path('admin/customuser/<pk>/delete/', admin.CustomUserAdmin.delete_view, name='customuser_delete'),
    path('login/', login_view, name='login'),
    path('signup/',signup_view,name='signup'),
]
