globalStop = 100


class person:
    def __init__(person, Wallet=0, name="Jan") -> None:  
        person.Wallet = Wallet
        person.name__ = name  # private attribute

    def ChargeAccount(person, AMOUNT) -> None:
        person.Wallet += AMOUNT

    @property
    def _get_name_(person) -> str:
        return person.name__

    def print_name(person) -> None:
        print(person._get_name_)


def CountTo(stop=globalStop) -> None:
    for I in range(stop):
        print(I)

def multiplicate(VAR_ONE, VAR_TWO,
                 VAR_THREE, VAR_FOUR):
    return VAR_ONE*VAR_TWO*VAR_THREE*VAR_FOUR


STOP = 40
CountTo(STOP)
STOP = 200
CountTo(STOP)


person_one = person(100, "Błażej", "I")
print(person_one._get_name_)
person_one.print_name()

varOne = 10
varTwo = 20
varThree = 30
varFour = 40
MultiplicatedVars = multiplicate(varOne, varTwo, varThree, varFour)
print(MultiplicatedVars)



    