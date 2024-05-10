from pathlib import Path

from environ import Env

# Load environment variables from `.env` file.
# https://django-environ.readthedocs.io/en/latest/

BASE_DIR = Path(__file__).parent.parent.parent

env = Env()
env.read_env(BASE_DIR / ".env")
