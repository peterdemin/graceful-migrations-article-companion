from django.db.models import Model, CharField


class Person(Model):
    full_name = CharField(max_length=128, null=True)
