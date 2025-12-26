import django
from django.conf import settings


def pytest_configure():
    import os
    import sys

    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

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
