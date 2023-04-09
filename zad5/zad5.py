def multiplicate(var_one, var_two,
                 var_three):
    #Takes three numbers and returns their product.
    return var_one*var_two*var_three


def concat(mess_one="Python", mess_two="Java"):
    """concat(mess_one, mess_two) -> mess_one + mess_two"""
    return mess_one + mess_two

def add_three(num="0"):
    """
    Input keyword: num (default: 0)
    Returns: Integer

    Takes number and returns this number increased by 3.
    """
    return num+3

"""Print documentation of multiplicate function."""
print(multiplicate.__doc__)
print(concat.__doc__) #print documentation of concat function
print(add_three.__doc__)  # Wyświetl dokumentację funkcji add_three