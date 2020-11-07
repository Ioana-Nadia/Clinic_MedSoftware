from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class clinicAccount(UserManager):
    def create_user(self, email, username, address, password=None):
        if not email:
            raise ValueError("Clinics must have an email address!")
        if not username:
            raise ValueError("Clinics must have a name!")
        user = self.model (
            email = self.normalize_email(email),
            username = username,
            address = address,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, address, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            address = address,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Clinic(AbstractUser):
    email = models.EmailField(max_length=60, verbose_name= 'email', unique=True, blank=False)
    username = models.CharField(max_length=30, blank=False)
    date_joined = models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    address = models.CharField(max_length=30, verbose_name= 'address', blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'address', ]
    objects = clinicAccount()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Patient(models.Model):
    patientsClinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length=30, blank=False)
    lastName = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=101, blank=True)
    phone = models.CharField(max_length=20, blank=False)
    cnp = models.CharField(max_length=15)
    allergies = models.CharField(max_length=250, default="No allergies")
    diseases = models.CharField(max_length=250, default="No diseases")
    currentTreatment = models.CharField(max_length=250, default="No treatment")
    def __str__(self):
        return self.email

class Intervention(models.Model):
    interventionsClinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True)
    interventionName = models.CharField(max_length=60, blank=False, unique=True)
    def __str__(self):
        return self.interventionName
