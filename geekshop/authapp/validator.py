from django.core.exceptions import ValidationError


def validate_name(value):
    if value.isdigit():
        raise ValidationError(
            (f"Имя не может состоять только из цифр"),
            params={'value': value}
        )
    if not value.isalpha():
        raise ValidationError(
            (f"Имя не может содержать цифры"),
            params={'value': value},
        )