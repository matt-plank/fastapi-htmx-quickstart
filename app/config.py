import os


def database_url() -> str:
    """Formatted database url string."""
    environment_variable = os.environ["DATABASE_URL"]

    if environment_variable.startswith("postgres://"):
        return environment_variable.replace("postgres://", "postgresql://", 1)

    return environment_variable
