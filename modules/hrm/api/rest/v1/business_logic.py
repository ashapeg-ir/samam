from uuid import uuid4

from django.conf import settings

from modules.common.utils import generate_random_numbers
from modules.common.redis_connection import rc

USERNAME_CODE_CACHE_KEY = 'samam_username_code:{username}'


class AuthBusinessV1:

    @classmethod
    def send_sms(cls, username):
        code = generate_random_numbers(n=4)
        cache_key = USERNAME_CODE_CACHE_KEY.format(username=username)
        rc.set(cache_key, code, ex=settings.SMS_CODE_EXPIRE_TIME)
        return code

    @classmethod
    def verify_sms_code(cls, username, code):
        cache_key = USERNAME_CODE_CACHE_KEY.format(username=username)
        cached_code = rc.get(cache_key)
        if cached_code and cached_code.decode('utf-8') == code:
            return True
        return False

    @classmethod
    def generate_user_code(cls, phone):
        uuid4_object = uuid4()
        h = uuid4_object.hex
        alpha = [i.upper() for i in h if i.isalpha()]
        result_alpha = ''.join(alpha)
        return result_alpha[:4] + phone[-4:]
