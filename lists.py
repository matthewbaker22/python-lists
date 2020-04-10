import random

'''
Print a message to the console indicating wether
each value of `number` is in the `my_randoms` list.
'''

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

numbers_1_to_10 = range(1, 11)

for number in numbers_1_to_10:
    the_numbers_match = False

    # Iterate your random number list here
    for rand_num in my_randoms:
        if rand_num == number:
            print("This number is in the randoms list:", number)
            the_numbers_match = True



