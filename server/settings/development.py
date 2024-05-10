from server.settings.base import *

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

# In development, we don't need a secure password hasher. We can use
# MD5 instead, this is because we don't need to worry about security
# in development. However, we should use a secure password hasher in
# production, like PBKDF2 or Argon2.

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
