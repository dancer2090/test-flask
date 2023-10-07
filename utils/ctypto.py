from constants import SECRET_KEY
from datetime import timedelta, datetime, timezone
import jwt


def is_valid_token(token):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if data:
            return True, data
        return False, None
    except Exception:
        return False, None


def generate_token(payload):
    payload["exp"] = datetime.now(tz=timezone.utc) + timedelta(hours=1)
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
