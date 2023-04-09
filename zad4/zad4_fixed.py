def divide(x, y):
    if (y == 0):
        return "Bad input argument"
    return x/y


def num(y):
    return y**2

my_bool = True
if (my_bool):
    print("My bool equals " + str(my_bool))

print(num(5))

if (not my_bool is False):
    my_bool = False

grades = [1, 2, 3, 4, 5, 6]
if grades:
    print("Grades list is correct")

print(not grades is my_bool)

print(divide(5, 0))