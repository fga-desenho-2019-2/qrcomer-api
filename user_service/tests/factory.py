
import factory
from ..api.utils.cpf import generate_cpf

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'user_service.Profile'

    cpf = generate_cpf()
    email = factory.Faker('email')
    password = factory.Faker('password', length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
    first_name = factory.Faker('first_name')
    birth_date = factory.Faker('date_of_birth', tzinfo=None, minimum_age=18, maximum_age=60)
    last_name = factory.Faker('last_name')
    sex = factory.Iterator(['m', 'f'])

