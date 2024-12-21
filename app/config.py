import os
from datetime import timedelta


def database_url() -> str:
    """Formatted database url string."""
    environment_variable = os.environ["DATABASE_URL"]

    if environment_variable.startswith("postgres://"):
        return environment_variable.replace("postgres://", "postgresql://", 1)

    return environment_variable


MAX_AUTH_SESSION_AGE: timedelta = timedelta(days=1)
MUST_USE_HTTPS: bool = os.environ["MUST_USE_HTTPS"] == "true"
