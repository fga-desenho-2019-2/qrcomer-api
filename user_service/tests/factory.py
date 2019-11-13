from ..api.utils.cpf import generate_cpf, generate_number
import factory, factory.fuzzy
from ..models import *

class UserFactory(factory.django.DjangoModelFactory):


    class Meta:
        model = Profile

    cpf = generate_cpf()
    email = factory.Faker('email')
    password = factory.Faker('password', length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
    first_name = factory.Faker('first_name')
    birth_date = factory.Faker('date_of_birth', tzinfo=None, minimum_age=18, maximum_age=60)
    last_name = factory.Faker('last_name')
    status_user = factory.fuzzy.FuzzyChoice([0,1])


class CardFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Card

    number = generate_number(16)
    cvv = generate_number(3)
    validation = factory.Faker('future_date', end_date="+720d", tzinfo=None)
    holder_name = factory.Faker('first_name')
    cpf_cnpj = generate_cpf()
    profile = factory.SubFactory(UserFactory)

