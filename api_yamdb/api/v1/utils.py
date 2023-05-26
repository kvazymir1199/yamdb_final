from django.conf import settings
from django.core.mail import send_mail


def send_confirmation_code(email, confirmation_code):
    """Отправляет код подтверждения на почту пользователя."""

    send_mail(
        'Регистрация на Yamdb',
        f'Используйте этот код {confirmation_code} для получения токена',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )
