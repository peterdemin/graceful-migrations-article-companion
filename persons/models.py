from django.db.models import Model, CharField
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Person(Model):
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    full_name = CharField(max_length=128, null=True)


@receiver(pre_save, sender=Person)
def update_full_name(sender, instance, **kwargs):
    instance.full_name = "{0} {1}".format(
        instance.first_name,
        instance.last_name,
    )
