# dice roll library, nate mckenzie, feb 18, 2021, 12:55, V0.99

# D4 sim
def roll_d4(num_roll): # num_roll = argument
    import random
    import time

    rolls = 0
    sum = 0
    while rolls < num_roll:
        result = random.randint(1,4)
        print(f"You rolled a {result} on the d4!\n")
        rolls += 1
        time.sleep(1)
        sum += result
    print(f"The total of your rolls was {sum}.\n")




#d6
def roll_d6(num_roll): # num_roll = argument
    import random
    import time

    rolls = 0
    sum = 0
    while rolls < num_roll:
        result = random.randint(1,6)
        print(f"You rolled a {result} on the d6!\n")
        rolls += 1
        time.sleep(1)
        sum += result
    print(f"The total of your rolls was {sum}.\n")





#d8
def roll_d8(num_roll): # num_roll = argument
    import random
    import time

    rolls = 0
    sum = 0
    while rolls < num_roll:
        result = random.randint(1,8)
        print(f"You rolled a {result} on the d8!\n")
        rolls += 1
        time.sleep(1)
        sum += result
    print(f"The total of your rolls was {sum}.\n")







#d20
def roll_d20(num_roll): # num_roll = argument
    import random
    import time

    rolls = 0
    sum = 0
    while rolls < num_roll:
        result = random.randint(1,20)
        print(f"You rolled a {result} on the d20!\n")
        rolls += 1
        time.sleep(1)
        sum += result
    print(f"The total of your rolls was {sum}.\n")







#d100
def roll_d100(num_roll): # num_roll = argument
    import random
    import time

    rolls = 0
    sum = 0
    while rolls < num_roll:
        result = random.randint(1,100)
        print(f"You rolled a {result} on the d100!\n")
        rolls += 1
        time.sleep(1)
        sum += result
    print(f"The total of your rolls was {sum}.\n")
