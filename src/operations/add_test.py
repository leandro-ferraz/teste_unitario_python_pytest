from .add import AddOperation
from faker import Faker

fake = Faker()

def test_soma():
    addOperation = AddOperation()
    number1 = fake.random_number()
    number2 = fake.random_number()

    result = addOperation.soma(number1, number2)
    assert result == 4+2