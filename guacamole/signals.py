from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    if instance.is_superuser:
        return
        
    if created:
        group, created = Group.objects.get_or_create(name='Posts')
        instance.groups.add(group)
