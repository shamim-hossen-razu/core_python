from django.contrib.auth.models import BaseUserManager, AbstractUser

class CustomUserManager(BaseUserManager):
    def create_user(self, email: str, password: str, **extra_fields):
        email = self.normalize_email(email)
        user: AbstractUser = self.model(email=email, **extra_fields)
        user.set_password(password) # hashes raw password and sets password field
        user.full_clean() # Trigger validation for model fields
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        # create superuser here
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        return self.create_user(email, password, **extra_fields)