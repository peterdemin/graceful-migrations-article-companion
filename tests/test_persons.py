import pytest

from persons.models import Person


@pytest.mark.django_db
def test_full_name_is_preserved():
    person = Person.objects.create(full_name="John Doe")
    assert person.full_name == "John Doe"
