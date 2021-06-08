from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    
    is_staffs= models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = CustomUserManager()



class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    dob =models.DateField(max_length=10)    
    designation = models.CharField(max_length=35)
    qualification = models.CharField(max_length=15)
    objects = models.Manager()

    def __str__(self):
        return self.phone_number




class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    
    address = models.TextField(max_length=100)
    dob =models.DateField(max_length=10)     
    mobile = models.CharField(max_length=15)
    District = models.CharField(max_length=20)
    qualification = models.CharField(max_length=35)
    college = models.CharField(max_length=30)
    course = models.CharField(max_length=35)
    objects = models.Manager()

    def __str__(self):
        return self.address





   

