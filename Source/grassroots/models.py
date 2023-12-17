from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
)
from django.utils.translation import gettext_lazy as _


########################################################################################################################
# THE CODE BETWEEN THE HASHES IS NOT BEING USED, BUT IS KEPT FOR REFERENCE, THE CODE BELLOW THIS BLOCK IS THE CURRENT CODE
class Person(models.Model):
    """Defines a Person Class Properties and Functions"""
    userID = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.TextField()

    def view_profile(self):
        """Allows a Person to view their details"""
        pass


class Customer(Person):
    """Defines a Customer Class Properties and Functions"""

    def apply_for_grant(self):
        """Creates a grant application for the Customer"""
        pass


class Admin(Person):
    """Admin functions to view and edit Customer grant applications"""

    def view_applications(self):
        """Returns all grant applications"""
        pass

    def edit_application(self):
        """Edits details of the grant application"""
        pass

    def view_customer(self):
        """Allows Admin to view a Customer"""
        pass


########################################################################################################################
# THIS IS THE MODELS USED IN THE CURRENT CODE
class UserManager(BaseUserManager):
    """
        Custom user manager for creating regular users and superusers.
        This manager is associated with the custom User model.
        The customer user model is a safer way to save user credentials.
        """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular user with the given email and password.

        :param email: The email address of the user.
        :param password: The password of the user.
        :param extra_fields: Extra fields to be saved with the user.
        :return: The created user object.
        """

        def create_user(self, email, password=None, **extra_fields):
            if not email:
                raise ValueError('The Email field must be set')
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a regular user with the given email and password.

        :param email: The email address of the user.
        :param password: The password for the user.
        :param extra_fields: Additional fields for the user.
        :return: The created User object.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model that uses email as the unique identifier for authentication.

    This model replaces the default Django User model and includes additional
    fields like first_name, last_name, phone, and address.
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="%(app_label)s_%(class)s_groups",
        related_query_name="%(app_label)s_%(class)ss",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="%(app_label)s_%(class)s_user_permissions",
        related_query_name="%(app_label)s_%(class)ss",
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """
        :return: a string representation of the user, typically the user's email address.
        """
        return self.email


class Grant(models.Model):
    """
    Model for a grant.
    Each grant has a name, amount, and description.
    """
    grantID = models.IntegerField(primary_key=True)
    grantName = models.CharField(max_length=255)
    grantAmount = models.FloatField()
    description = models.TextField()

    def view_applications(self):
        """View Grant application"""
        pass


class SpecialAward(models.Model):
    """
    Details of a special award

    Each special award has a name, description, eligibility, detail, and status.
    """
    awardID = models.IntegerField(primary_key=True)
    awardName = models.CharField(max_length=255)
    description = models.TextField()
    eligibility = models.CharField(max_length=255)
    detail = models.TextField()
    status = models.CharField(max_length=255)

    def apply_for_special(self):
        """Create a special award application"""
        pass


class Application(models.Model):
    """
    Details of an application
    Each application has an applicant, grant, award, detail, and status.
    """
    appID = models.IntegerField(primary_key=True)
    applicant = models.ForeignKey(Customer, on_delete=models.CASCADE)
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE)
    # Assuming the Award referenced here is the SpecialAward model
    award = models.ForeignKey(SpecialAward, on_delete=models.CASCADE, null=True, blank=True)
    detail = models.TextField()
    status = models.CharField(max_length=255)

    def submit_application(self):
        """Submitting an Application"""
        pass

    def view_status(self):
        """Returns the Applications status"""
        pass


