from ..api.utils.cpf import generate_cpf, generate_number_card
import factory.fuzzy


class UserFactory(factory.django.DjangoModelFactory):
    STATUS = (
        (0, True),
        (1, False),
    )
    STATUS_ID = [x[0] for x in STATUS]

    class Meta:
        model = 'user_service.Profile'

    cpf = generate_cpf()
    email = factory.Faker('email')
    password = factory.Faker('password', length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
    first_name = factory.Faker('first_name')
    birth_date = factory.Faker('date_of_birth', tzinfo=None, minimum_age=18, maximum_age=60)
    last_name = factory.Faker('last_name')
    status_user = factory.fuzzy.FuzzyChoice(STATUS_ID)


class CardFactory(factory.django.DjangoModelFactory):
    STATUS = (
        (0, True),
        (1, False),
    )
    STATUS_ID = [x[0] for x in STATUS]

    class Meta:
        model = 'user_service.Card'

    number = generate_number_card()
    cvv = factory.Faker(length=3, digits=True)
    validation = factory.Faker('validation', tzinfo=None)
    holder_name = factory.Faker('first_name')
    cpf_cnpj = generate_cpf()
    profile = factory.Faker('profile__email')
