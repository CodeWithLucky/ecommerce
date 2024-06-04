from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login
from .models import CustomUser

User = get_user_model()

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


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)  
        user = authenticate(email=email, password=password)
        if user is not None:
            
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'sign-in.html', {'error': 'Email or Password is incorrect'})              
    return render(request, 'login.html')
    
def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        sex = request.POST['selected']
        date_of_birth = request.POST['dateofbirth']
        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,sex=sex,date_of_birth=date_of_birth,password=password)
        print(user)
        user.save()
        return redirect('login')

    return render(request,'signup.html')