from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import PostCategory
from .tasks import post_created


@receiver(m2m_changed, sender=PostCategory)
def signal_post_created(instance, sender, **kwargs):
    post_created.delay(instance.id)