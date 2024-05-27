from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import UserInfo, AccountInfo, Role
from . form import UserForm, AccountInfoForm, RoleForm

class UserListView(View):
    def get(self, request):
        users = UserInfo.objects.all()
        return render(request, 'user_list.html', {'users': users})

class UserDetailView(View):
    def get(self, request, user_id):
        user = get_object_or_404(UserInfo, id=user_id)
        return render(request, 'user_detail.html', {'user': user})

class UserCreateView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'user_create.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, 'user_create.html', {'form': form})

class UserUpdateView(View):
    def get(self, request, user_id):
        user = get_object_or_404(UserInfo, id=user_id)
        form = UserForm(instance=user)
        return render(request, 'user_update.html', {'form': form, 'user': user})

    def post(self, request, user_id):
        user = get_object_or_404(UserInfo, id=user_id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, 'user_update.html', {'form': form, 'user': user})

class UserDeleteView(View):
    def get(self, request, user_id):
        user = get_object_or_404(UserInfo, id=user_id)
        return render(request, 'user_delete.html', {'user': user})

    def post(self, request, user_id):
        user = get_object_or_404(UserInfo, id=user_id)
        user.delete()
        return redirect('user_list')

class AccountListView(View):
    def get(self, request):
        accounts = AccountInfo.objects.all()
        return render(request, 'account_list.html', {'accounts': accounts})

class RoleListView(View):
    def get(self, request):
        roles = Role.objects.all()
        return render(request, 'role_list.html', {'roles': roles})
