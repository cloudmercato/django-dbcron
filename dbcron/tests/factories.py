from faker import Faker
import factory
from factory import fuzzy

faker = Faker()


class JobFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('job')
    tag = factory.Faker('name')
    func = 'django.utils.timezone.now'

    sec = 0
    min = fuzzy.FuzzyInteger(0, 59)
    hou = fuzzy.FuzzyInteger(0, 23)
    dom = '*'
    mon = '*'
    dow = '*'
    yea = '*'

    class Meta:
        model = 'dbcron.Job'
