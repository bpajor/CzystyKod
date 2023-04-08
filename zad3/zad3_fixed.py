GLOBAL_STOP = 100


class Person:
    def __init__(self, wallet=0, name="Jan") -> None:  
        self.wallet = wallet
        self.__name = name  # private attribute

    def charge_account(self, amount) -> None:
        self.wallet += amount

    @property
    def __get_name(self) -> str:
        return self.__name

    def print_name(self) -> None:
        print(self.__get_name)


def count_to(stop=GLOBAL_STOP) -> None:
    for i in range(stop):
        print(i)

def multiplicate(var_one, var_two,
                 var_three, var_four):
    return var_one*var_two*var_three*var_four


stop = 40
count_to(stop)
stop = 200
count_to(stop)


person_one = Person(100, "Błażej")
# print(person_one._get_name_)
person_one.print_name()

var_one = 10
var_two = 20
var_three = 30
var_four = 40
multiplicated_vars = multiplicate(var_one, var_two, var_three, var_four)
print(multiplicated_vars)