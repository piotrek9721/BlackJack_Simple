import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_on = False
print(logo)

first_card = input("do you want to play? ")

if first_card == 'yes':
    deck_comp = 0
    deck_player = 0
    game_on = True
else:
    print("Okey, see you next time")
    SystemExit()

while game_on:
    point_player = random.randint(0, len(cards)-1)
    point_comp = random.randint(0, len(cards) - 1)
    another_card = input("Do you want to draw a card?")
    deck_comp += cards[point_comp]
    deck_player += cards[point_player]
    print(f"Your score is {deck_player}")
    if another_card == 'yes':
        if deck_comp == 21:
            print(f"Dealer score is {deck_comp}")
            print("Dealer wins!")
            game_on = False
        elif deck_player == 21:
            print(f"Dealer score is {deck_comp}")
            print("Player wins!")
            game_on = False
        elif deck_player > 21:
            print(f"Dealer score is {deck_comp}")
            print("Dealer wins!")
            game_on = False
        elif deck_comp > 21:
            print(f"Dealer score is {deck_comp}")
            print("Player wins!")
            game_on = False
        else:
            game_on = True
    else:
        if deck_player < deck_comp:
            print(f"Dealer score is {deck_comp}")
            print("Dealer wins!")
            game_on = False
        elif deck_player == deck_comp:
            print(f"Dealer score is {deck_comp}")
            print("Draw!")
            game_on = False
        else:
            print("Player wins!")
            print(f"Dealer score is {deck_comp}")
            game_on = False


