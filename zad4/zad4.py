def divide(x, y):
    if (y == 0):
        return
    return x/y

my_bool = True
if (my_bool == True):
    print("My bool equals " + str(my_bool))

num = lambda y: y**2
print(num(5))

if (my_bool is not False):
    my_bool = False

grades = [1, 2, 3, 4, 5, 6]
if len(grades):
    print("Grades list is correct")

print(not len(grades) is my_bool)

print(divide(5, 4))




