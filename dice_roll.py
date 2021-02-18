# dice roll library, nate mckenzie, feb 18, 2021, 12:22, V0.01

# D4sim
def roll_d4(num_roll): # num_roll = argument
    import random
    
    rolls = 0
    while rolls <= num_roll:
        result = random.randint(1,4)
        print(f"You rolled a {result} on the d4!\n")
        rolls += 1

