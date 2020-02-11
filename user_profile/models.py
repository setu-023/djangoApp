# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
#
#
#
#
#
# class MyAccountManager(BaseUserManager):
# 	def create_user(self, email, username, password=None):
# 		if not email:
# 			raise ValueError('Users must have an email address')
# 		if not username:
# 			raise ValueError('Users must have a username')
# 		# if not role:
# 		# 	raise ValueError('Users must have a role')
#
# 		user = self.model(
# 			email=self.normalize_email(email),
# 			username=username,
# 			#role=role,
#
# 		)
#
# 		user.set_password(password)
# 		user.save(using=self._db)
# 		return user
#
# 	def create_superuser(self, email, username, password):
# 		user = self.create_user(
# 			email=self.normalize_email(email),
# 			password=password,
# 			username=username,
# 		)
# 		user.is_admin = True
# 		user.is_staff = True
# 		user.is_superuser = True
# 		user.save(using=self._db)
# 		return user
#
# #
# # class Profile(AbstractBaseUser):
# # 		email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
# # 		username 				= models.CharField(max_length=30, unique=True)
# # 		role 					= models.CharField(max_length=30,)
# #
# # 		objects = MyAccountManager()
# #
#
#
# class User_Profile(models.Model):
#
#     username = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )
# 	email 					= models.EmailField(max_length=60, unique=True)
# 	username 				= models.CharField(max_length=30, unique=True)
# 	#role					= models.CharField(max_length=60, default= 'manager' )
# 	#phn						= models.CharField(max_length=30, unique=True)
#
# 	USERNAME_FIELD = 'email'
# 	REQUIRED_FIELDS = ['username']
#
# 	objects = MyAccountManager()
#
# 	def __str__(self):
# 		return self.username
#
# 	# For checking permissions. to keep it simple all admin have ALL permissons
# 	def has_perm(self, perm, obj=None):
# 		return self.is_admin
#
# 	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
# 	def has_module_perms(self, app_label):
# 		return True
#
#
# 	class Meta:
# 		verbose_name = ('user_profile')
#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)