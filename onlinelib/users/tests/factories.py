from django.contrib.auth import get_user_model

import factory
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda o: f'{o.username}@test.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create or not extracted:
            return None

        return self.groups.add(*extracted)

    class Meta:
        model = get_user_model()

    class Params:
        admin = factory.Trait(is_staff=True, is_superuser=True)