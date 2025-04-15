import random
choose1= ['r', 'p', 's']


cont_play= input('Do you wish to play? y/n') # Make a choice, continue to play

while cont_play == 'y':
    comp1= random.choice(choose1)
    self_choice= input('Choose r (rock), p (paper), s (scissors)')
    if self_choice not in choose1:
        print('Invalid choice!')

    if self_choice == comp1:
        print('Draw reached')
    elif self_choice == 'r':
        if comp1 == 'p':
            print('You lose! Paper beats rock')
        elif comp1 == 's':
            print('You win! Rock beats scissors')
    elif self_choice == 'p':
        if comp1 == 'r':
            print('You win! Paper beats rock')
        elif comp1 == 's':
            print('You lose! Scissors beats paper')
    elif self_choice == 's':
        if comp1 == 'r':
            print('You lose! Rock bears scissors')
        elif comp1 == 'p':
            print('You win! Scissors beats paper')
    cont_play = input('Do you wish to continue to play? y/n') # Make a choice, continue to play
    if cont_play == 'n':
        print('Game has ended')
