from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, sex, password=None, date_of_birth=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            sex=sex,
            date_of_birth=date_of_birth,
            last_name=last_name,
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        user = self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
