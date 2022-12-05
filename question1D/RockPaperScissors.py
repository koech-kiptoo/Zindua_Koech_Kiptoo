import random
your_points  = 0
computer_points = 0

# initializing list
rounds = [3, 5]
rand_idx = random.randrange(len(rounds))
random_num = rounds[rand_idx]
print('Random', random_num)
# printing random number
for i in range(0,random_num):
    if computer_points == 2:
        print('Computer wins with ', computer_points, 'Points')
        exit(0)
        break


    elif your_points == 2:
        print('You win with ', your_points, 'Points')
        exit(0)
        break

    else:
        user_action = input("Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        if user_action == "rock":
            if computer_action == "scissors":
                #print("Rock Beats scissors!")
                your_points = your_points + 1
            else:
                computer_points = computer_points + 1
                #print("Paper beats rock!")
        elif user_action == "paper":
            if computer_action == "rock":
                your_points = your_points + 1
                #print("Paper beats rock!")
            else:
                computer_points = computer_points + 1
                #print("Scissors beats paper!")
        elif user_action == "scissors":
            if computer_action == "paper":
                your_points = your_points + 1
                #print("Scissors beats paper!")
            else:
                computer_points = computer_points + 1
                #print("Rock beats scissors!")

if computer_points > your_points:
    print('Computer wins with ', computer_points, 'Points')

elif your_points > computer_points:
    print('You win with ', your_points, 'Points')

elif computer_points == your_points:
    print('There is a tie of Computer :', computer_points, 'Your Points ', your_points)