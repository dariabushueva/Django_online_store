from django.conf import settings
from django.core.mail import send_mail


def send_verification_email(email, url):
    send_mail(
        subject='Подтверждение регистрации',
        message=f'Для завершения регистрации, пожалуйста, перейдите по ссылке: {url}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )
