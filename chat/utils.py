import jwt
from django.conf import settings
from django.contrib.auth.models import User
from channels.db import database_sync_to_async

@database_sync_to_async
def get_user_from_jwt(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("user_id")
        
        return User.objects.get(id=user_id)
    except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist, Exception) as e:
        print(f"JWT Auth Error: {e}")
        return None