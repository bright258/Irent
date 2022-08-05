# in buiilt django dependencies
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _


# manager
class CustomManager(UserManager):

    def create_user(self, username, email  , password , **extra_fields):

        if not email:
            raise ValueError(_('Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()


        return user