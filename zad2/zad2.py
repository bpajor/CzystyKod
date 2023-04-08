import random


def slice_basket(list:list, start  :int, stop :int)  ->list    :
    return list[start :stop]

def define_very_important_variables()->list:
    x =                   1
    y=2
    z =3
    print(x, y ,z,)

fruits_basket = [ {'apple' : 1} , {'orange'  : 2} ,  {'banana': 3},]
print(fruits_basket[ random.randint(0, 2)   ])

vegetables_basket = { 'carrots': 1,   'potatoes':6}

vegetables_amount=0
for key ,value in vegetables_basket.items() :
    vegetables_amount+=value

print((vegetables_amount * 2) + 5            )

fruits_basket.append( {'strawberries' : 2})
print(slice_basket(fruits_basket, 1,  4))

another_list = [slice_basket(fruits_basket,2,3) for  i in range(100) if (i%2==0 and i<40)]
another_list.append([1,         2,3,          5,6,7 , 8,])
another_list.append((0,))
print(another_list)
