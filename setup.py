from setuptools import setup

setup(
    name="sentry-flake8",
    version="0.0.1",
    description="Sentry's custom flake8 checker plugin.",
    license="Apache 2.0",
    url="https://github.com/getsentry/sentry-flake8",
    author='Sentry',
    author_email='hello@sentry.io',
    install_requires=[
        "flake8>=3.5.0,<3.6.0",
    ],
    py_modules=['sentry_check'],
    entry_points={
        "flake8.extension": [
            "B = sentry_check:SentryCheck",
        ]
    },
)
