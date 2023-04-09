def multiplicate(var_one, var_two,
                 var_three):
    """Takes three numbers and returns their product."""
    return var_one*var_two*var_three


def concat(mess_one="Python", mess_two="Java"):
    """Takes two arguments and returns concatenation of them"""
    return mess_one + mess_two

def add_three(num=0):
    """
    Takes number and returns this number increased by 3.

    Input keyword: num (default: 0)
    Returns: Integer
    """
    return num+3

print(multiplicate.__doc__)  # Print documentation of multiplicate function.
print(concat.__doc__) #Print documentation of concat function.
print(add_three.__doc__)  # Print documentation of add_three function.