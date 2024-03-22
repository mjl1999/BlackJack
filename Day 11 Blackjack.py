from time import sleep
from secrets import choice


def convert_aces(hand):
    if sum(hand) > 21:
        for index in range(len(hand)):
            if hand[index] == 11:
                hand[index] = 1
                if sum(hand) <= 21:
                    return hand
                else:
                    continue
        return hand
    else:
        return hand


def hand_cards(cards):
    user_hand = []
    comp_hand = []
    for index in range(2):
        user_hand.append(choice(cards))
        comp_hand.append(choice(cards))
    return convert_aces(user_hand), convert_aces(comp_hand)


def display_start(user, comp):
    print("Your hand: ", end="")
    for index in range(len(user)):
        print(f"{user[index]} ", end="")
    print(f"\nComputer's Hand: {comp[0]} {'[_]' * (len(comp) - 1)}")


def display_user(user):
    for index in range(len(user)):
        print(f"{user[index]} ", end="")


def gone_bust(hand):
    if sum(hand) > 21:
        return True
    else:
        return False


def black_jack(hand):
    if sum(hand) == 21:
        return True
    else:
        return False


def add_card(hand, cards):
    hand.append(choice(cards))
    return convert_aces(hand)


def evaluate_user(hand):
    sleep(1)
    if black_jack(hand):
        print("BlackJack! Let's see the computer's cards... \n")
    elif gone_bust(hand):
        print("You've gone bust! Let's hope the computer does too: \n")
    else:
        print(f"Will {sum(hand)} be enough to win? \n")


def result(user, comp):
    print(f"\nYour hand: {sum(user)} | Computer's hand: {sum(comp)}")
    sleep(1)
    if black_jack(user) and black_jack(comp):
        print("Draw! You both got blackjack!")
    elif black_jack(user):
        print("You win! Blackjack!")
    elif gone_bust(user) and gone_bust(comp):
        print("Draw! You both went bust!")
    elif gone_bust(comp) and not gone_bust(user):
        print("You win! Computer went bust!")
    elif sum(user) > sum(comp) and not gone_bust(user):
        print("You win!")
    else:
        print("You lose!")


def play_again(answer):
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        return play_again(input("Invalid option, please type 'yes' or 'no': ").lower())


def check_choice(option):
    if option != "hit" and option != "stand":
        return check_choice(input("Not an option - please choose 'Hit' or 'Stand': ").lower())
    else:
        return option


def display_comp(comp):
    sleep(1)
    print(f"Computer's hands: {comp[0]}", end=" ")
    for i in range(1, len(comp)):
        sleep(1)
        print(comp[i], end=" ")
    print()


deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while True:
    # Hands out the user and computer's starting cards
    # Display the two starting cards for both user and comp, but obscuring the computer's second card
    user_deck, comp_deck = hand_cards(deck)
    display_start(user_deck, comp_deck)

    # while the user hasn't gone bust or gotten blackjack and has less than 5 cards:
    # ask the user if they wish to draw another card: Add a card if yes | Continue with the game if not.
    while sum(user_deck) < 21 and len(user_deck) != 5:
        user_choice = check_choice(input(f"Your total is: {sum(user_deck)} | 'Hit' or 'Stand': ").lower())
        if user_choice == "hit":
            user_deck = add_card(user_deck, deck)
            print(f"Total: {sum(user_deck)} | {user_deck}")
        else:
            break

    # check to see the status of the user's final hand and then print out a resulting message before proceeding
    evaluate_user(user_deck)

    # get the computer to draw a card when it has less than 5 cards and sum is less than 17
    while sum(comp_deck) < 17 and len(comp_deck) < 5:
        comp_deck = add_card(comp_deck, deck)
    # if the computer < 21, and comp < user, and the user hasn't gone bust, the computer must draw again if len < 5
    while sum(comp_deck) < 21 and not gone_bust(user_deck) and sum(comp_deck) < sum(user_deck) and len(comp_deck) < 5:
        comp_deck = add_card(comp_deck, deck)

    # print out the computer's hands one by one
    display_comp(comp_deck)

    # print the result
    sleep(1.5)
    result(user_deck, comp_deck)

    # ask user if they wish to play again
    sleep(1.5)
    if play_again(input("\nWould you like to play again - 'yes' or 'no'?: ").lower()):
        print()
        continue
    else:
        print("Thank you for playing!")
        quit()
