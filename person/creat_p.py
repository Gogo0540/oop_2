from .models import Person



def create(name, last, age):
    person = Person(
        name=name,
        last=last,
        age=age

    )

    return person
