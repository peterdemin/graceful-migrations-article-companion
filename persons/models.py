from django.db.models import Model, CharField


class Person(Model):
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)