from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    pass

# Update user profile if user created

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         User.objects.create_user(username=instance)

# Update user profile if user is saved
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# class Users(models.Model):
#     user_id = models.BigAutoField(primary_key=True)
#     username = models.CharField(max_length=30, blank=False)
#     email = models.EmailField(max_length=75, unique=True, blank=False)
#     # password = PasswordInput()
#     date_created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = "Users"

#     def __str__(self):
#         return self.username