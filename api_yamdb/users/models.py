from django.contrib.auth.models import AbstractUser
from django.db import models

CUT_TEXT = 15


class User(AbstractUser):
    """
    Кастомная модель.
    Расширена дополнительными полями.
    """

    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLES = (
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    )
    username = models.CharField(
        'Логин',
        max_length=150,
        unique=True,
        blank=False, null=False,
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=254,
        unique=True,
        blank=False
    )
    bio = models.TextField(
        'Биография',
        null=True,
        blank=True
    )
    role = models.CharField(
        'Роль пользователя',
        max_length=9,
        choices=ROLES,
        default=USER,
        blank=False,
        null=False,
    )
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=30,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_user_email'
            ),
        ]

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser or self.is_staff

    def __str__(self):
        return self.username[:CUT_TEXT]
