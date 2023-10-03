from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.backends import ModelBackend

from rest_framework_simplejwt.exceptions import AuthenticationFailed

from modules.hrm.api.rest.v1.business_logic import AuthBusinessV1

User = get_user_model()


class CustomerPhoneLoginOrRegisterBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        username = username
        if AuthBusinessV1.verify_sms_code(username=username, code=password):
            try:
                user = User.objects.get(username=username, is_customer=True)
            except User.DoesNotExist:
                user = User.objects.create(
                    username=username,
                    is_active=True,
                    is_customer=True,
                )
        else:
            raise AuthenticationFailed(
                _('Your OTP Password has been expired or is wrong')
            )
            return None
        if user.is_active:
            return user
        return None


# TODO: select user from appropriate organization and department who is active and has a job
def user_authenticate(request, username, password, **kwargs):

    try:
        user = User.objects.get(username=username, is_active=True, is_verified=True, is_customer=False)
    except User.DoesNotExist:
        raise AuthenticationFailed(
            _("dear user you are not active or you are not part of the system please contact the administrator.")
        )
    else:
        if user.check_password(password):
            return user
    return None
