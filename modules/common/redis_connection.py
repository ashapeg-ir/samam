from django.conf import settings

import redis

rc = redis.Redis(
    host=settings.REDIS_ADDRESS,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DBNAME,
    username=settings.REDIS_USERNAME,
    password=settings.REDIS_PASSWORD,
)
