from django.contrib.auth.base_user import BaseUserManager
import random

#from rest_framework.fields import SerializerMethodField
class UserManager(BaseUserManager):
    use_in_migrations=True
    def create(self,mobileNumber,**extra_fields):
        if mobileNumber:
            user=self.model(mobileNumber,**extra_fields)

            otp=random.randint(999,9999)
            user.otp=otp
            user.save(using=self._db)
            return user
        else:
            raise ValueError('mobile number is required')

    # def create_staffuser(self,email,password):
    #     user=self.create_user(
    #         email,
    #         password=password,
    #     )
    #     user.staff=True
    #     user.save(using=self._db)
    #     return user
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff is true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user have is_superuser is true')
        return self.create(email,password,**extra_fields)