import secrets
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, FileExtensionValidator
from django.utils.translation import gettext_lazy as _text
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver
from utils.handle_file import checkFileExists
from .user_manager import CustomUserManager

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(limit_value=0, message="Votes cannot be negative")
        ],
    )
    voters = models.ManyToManyField("User")


class User(AbstractUser):
    first_name = models.CharField(_text("first name"), max_length=150)
    last_name = models.CharField(_text("last name"), max_length=150)
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": _text("A user with that email already exists."),
        },
    )
    username = models.SlugField(
        unique=True,
        max_length=200,
        blank=True,
        editable=False,
        error_messages={
            "unique": _text("A user with that username already exists."),
        },
    )
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)
    photo = models.ImageField(
        _text("profile photo"),
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"])],
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()
    
    def _create_username(self):
        name = self.get_full_name()[:200]
        return slugify(name + "-" + str(secrets.randbits(32)))
    
    def save(self, *args, **kwargs):
        if not self.username or \
            any(map(lambda key: key in kwargs, ("first_name","last_name"))):
            self.username = self._create_username()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username


@receiver(post_delete, sender=User)
def delete_user_photo(sender, instance: User, *args, **kwargs):
    """Delete file field when model instance or queryset is deleted"""
    if instance.photo and checkFileExists(instance.photo.path):
        instance.photo.delete()
