"""
Local database abstraction layer for step defs.
"""


from django.contrib.auth.models import User
from election.models import Election


def count_users():
    return User.objects.count()


def count_polls():  # TBD: "scrutin" translates to "poll"?
    return Election.objects.count()


def find_user(identifier):
    user = User.objects.get(username=identifier)
    if user is not None:
        return user
    raise ValueError("No user found matching `%s`." % identifier)