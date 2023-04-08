import math, random

class Car:
        instances=0
        def __init__(self):
         print("This is Car")
         Car.instances+=1
        def drive(self):
                print("Driving")
        def instances_amount(self):
            print(Car.instances)





def print_message(message_one, message_two,
    message_three):
    message_to_print = (message_one + 
                        message_two +
                        message_three)
    print(message_to_print)
def add(number_one,
    number_two):
      return (number_one + 
              number_two)


def if_statement(number):
    if (number > 60):
               return number
    return 40

message_one = "This is message which length is about 110 chars. It definitely doesn't help to improve readiblity of this code"
message_two = "Try to fixed it" + ', using clean code'
message_three = " rules."

print_message(message_one,
message_two, message_three)

for i in range(20):
               number = add(math.sqrt(100), random.randint(1,100))
               number_to_print = if_statement(number)
               print(number_to_print)

car_1 = Car()
car_1.drive()
car_2 = Car()
car_2.instances_amount()


