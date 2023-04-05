from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class UserData(AbstractUser):
    username = None
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class Vinyl(models.Model):
    release = models.CharField(max_length=24, verbose_name='Release Discogs', null=True, blank=True)
    artist = models.CharField(max_length=80, verbose_name='Artist')
    album = models.CharField(max_length=80, verbose_name='Album')
    genres = models.CharField(max_length=80, verbose_name='Genres', null=True, blank=True)
    styles = models.CharField(max_length=80, verbose_name='Styles', null=True, blank=True)
    notes = models.TextField(verbose_name='Notes', null=True, blank=True)
    formats = models.CharField(max_length=24, verbose_name='Formats', null=True, blank=True)
    qty = models.CharField(max_length=8, verbose_name='Qty', null=True, blank=True)
    manufacture_region = models.CharField(max_length=80, verbose_name='Manufacture region', null=True, blank=True)
    label = models.CharField(max_length=80, verbose_name='Label', null=True, blank=True)
    catalogue_number = models.CharField(max_length=80, verbose_name='Catalogue number', null=True, blank=True)
    year = models.CharField(max_length=80, verbose_name='Year', null=True, blank=True)
    average_rating = models.CharField(max_length=80, verbose_name='Average rating', null=True, blank=True)
    owners_number = models.DecimalField(max_digits=80, decimal_places=0, verbose_name='Owners', null=True, blank=True)
    sell_number = models.DecimalField(max_digits=80, decimal_places=0, verbose_name='Sell', null=True, blank=True)
    lowest_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Lowest price, USD', null=True,
                                       blank=True)
    image = models.ImageField(verbose_name='Image', null=True, blank=True)
    image_url = models.CharField(max_length=255, verbose_name='Image URL', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Added to collection')
    owner = models.ForeignKey(UserData, on_delete=models.SET_NULL, null=True, blank=True)
    user_rating = models.CharField(max_length=2, verbose_name='User rating', null=True, blank=True)

    def __str__(self):
        return f'{self.catalogue_number}'
