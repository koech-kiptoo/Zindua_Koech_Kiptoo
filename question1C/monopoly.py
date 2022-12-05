import random
# let's create a loop so it keeps allowing us to roll the dice
def roll():
    total = 0
    count = 0
    while True:
        # next, we will roll two random dice from 1 to 6
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print(d1)
        print(d2)

        # let's determine if doubles are rolled
        if d1 == d2:
            count = count + 1
            if count == 3:
                print('Go to Jail')
                break
            else:
                print("Doubles! Roll again!")
                print("Press enter to roll again")
                total = (d1 + d2)

        else:
            total += (d1  + d2)
            print("The sum of the dice is ", total)
            break


roll()
