from secrets import choice
from time import sleep


def gone_bust(hand):
    return sum(hand) > 21


def convert_aces(hand):
    if gone_bust(hand):
        for i in range(len(hand)):
            if hand[i] == 11:
                hand[i] = 1
                if not gone_bust(hand):
                    break
    return hand


def give_hand(deck):
    hand = []
    for _ in range(2):
        hand.append(choice(deck))
    hand = convert_aces(hand)
    return hand


def black_jack(hand):
    return sum(hand) == 21


def display_hands(player, comp):
    hidden_cards = "[_]" * (len(comp) - 1)
    print(f"Computer's hand: {comp[0]} {hidden_cards}")
    print(f"Your hand: ", end="")
    for i in range(len(player)):
        print(f"{player[i]} ", end="")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand, computer_hand = give_hand(cards), give_hand(cards)

# allow the user to hit or stand
while len(user_hand) != 5 and not black_jack(user_hand) and not gone_bust(user_hand):
    display_hands(user_hand, computer_hand)
    decision = input("Hit or Stand?: ").lower()
    while decision != "hit" and decision != "stand":
        decision = input("Not a valid option! Please choose 'Hit' or 'Stand': ")
    if decision == "hit":
        user_hand.append(choice(cards))
        user_hand = convert_aces(user_hand)
    else:
        break

# display and respond to the state of the user's hand
display_hands(user_hand, computer_hand)
if gone_bust(user_hand):
    print(f"\n{sum(user_hand)}! You've gone bust! Let's hope the dealer does too!")
elif black_jack(user_hand):
    print(f"\nYou got Blackjack! Let's see the dealer's hand!")
else:
    print(f"\nYour hands total is: {sum(user_hand)}! Let's hope it's enough to beat the dealer")

# Under the following criteria, force the computer to draw a hand
while len(computer_hand) != 5 and sum(computer_hand) < 17:
    computer_hand.append(choice(cards))
    computer_hand = convert_aces(computer_hand)
while len(computer_hand) != 5 and sum(computer_hand) < sum(user_hand) and not gone_bust(user_hand):
    computer_hand.append(choice(cards))
    computer_hand = convert_aces(computer_hand)

# Show the computer's hand one by one
print("Computer's hand: ", end="")
for card in computer_hand:
    sleep(1)
    print(card, end=" ")

# Show the result of the game
print(f"\nYour hand: {sum(user_hand)} |   Computer's hand: {sum(computer_hand)}")
if gone_bust(computer_hand) and gone_bust(user_hand):
    print("Draw! You have both gone bust!")
elif gone_bust(computer_hand):
    print("You win! Dealer went bust! ")
elif gone_bust(user_hand):
    print("You lose! Dealer didn't go bust!")
elif sum(user_hand) == sum(computer_hand):
    print("Draw!")
elif sum(user_hand) < sum(computer_hand):
    print("You lose! Dealer didn't go bust!")
else:
    print("You win! You had the greater hand!")
