from django.core.exceptions import ValidationError
from django.utils import timezone


def deadline_validator(value):
    if value < timezone.now():
        raise ValidationError(
            '%(value)s is not a correct deadline!',
            params={'value': value},
        )