import random
def even_or_odd(die):
    if int(die) % 2 == 0:
        return 1
    return 0
def create_pattern(die,a):
    if a == 0:
        for i in range(int(die) + 1, 0, -1):
            for j in range(0, i - 1):
                print("*", end=' ')
            print(" ")
    else:
        for i in range(0, int(die)):
            for j in range(0, i + 1):
                print("* ", end="")
            print()

def roll_die():
    repeat = True
    while repeat:
        die = str(random.randint(1,6))
        print("Rolled, you got",die)
        a = even_or_odd(die)
        create_pattern(die,a)
        print("You want to roll again?,Print \"Yes\" else enter any key")

        repeat = "Yes" in input()
roll_die()
