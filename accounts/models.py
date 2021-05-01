from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, blank=True, validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
    gender = models.CharField(max_length=1, blank=True, choices=GenderChoices.choices, default=GenderChoices.MALE)
    avatar = models.ImageField(blank=True, upload_to="accounts/avatar/%Y/%m/%d",
                               help_text="48px * 48px 크기의 png 또는 jpg 파일을 업로드해주세요.")  # FIXME: Improve this by using django-imagekit.

# class Profile(models.Model):
#     pass
