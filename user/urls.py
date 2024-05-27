from django.urls import path
from .views import (
    UserListView, UserDetailView, UserCreateView,
    UserUpdateView, UserDeleteView, AccountListView,
    RoleListView
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('user/<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('user/update/<int:user_id>/', UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:user_id>/', UserDeleteView.as_view(), name='user_delete'),
    path('accounts/', AccountListView.as_view(), name='account_list'),
    path('roles/', RoleListView.as_view(), name='role_list'),
]
