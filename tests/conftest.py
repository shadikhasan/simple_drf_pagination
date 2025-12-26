import django
from django.conf import settings


def pytest_configure():
    if not settings.configured:
        settings.configure(
            DEBUG=True,
            SECRET_KEY="test",
            ALLOWED_HOSTS=["testserver", "localhost", "127.0.0.1"],
            INSTALLED_APPS=[
                "django.contrib.contenttypes",
                "django.contrib.auth",
                "rest_framework",
            ],
            DATABASES={
                "default": {
                    "ENGINE": "django.db.backends.sqlite3",
                    "NAME": ":memory:",
                }
            },
            REST_FRAMEWORK={
                "PAGE_SIZE": 10
            },
        )
        django.setup()
