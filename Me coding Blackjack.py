from random import choice
import time


def main():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # deal the first two cards to the user and computer
    player_hand, computer_hand = starting_cards(cards)
    player_hand, computer_hand = convert_aces(player_hand), convert_aces(computer_hand)
    # display the cards of both the computer and user, but obscure the computer's second card
    display_hands(player_hand, computer_hand)
    # So long as the user has not got five cards and has not gone bust, keep asking if they want to hit or stand
    while len(player_hand) != 5:
        if bust(player_hand) or black_jack(player_hand):
            break
        if hit(input("Hit or Stand? -> ").lower()):
            player_hand = add_card(player_hand, cards)
            player_hand = convert_aces(player_hand)
            display_hands(player_hand, computer_hand)
        else:
            break
    print(f"\nYour final hand is: {sum(player_hand)}")
    time.sleep(2)
    if black_jack(player_hand):
        print("Black Jack! You win!")
        if play_again():
            main()
    elif bust(player_hand):
        print("\nYou've gone bust! let's hope the computer does too...")
    else:
        print("Let's hope it's enough...\n")
    time.sleep(2)

    # have the computer keep drawing cards while they have less than 5 cards AND lower than 17
    print(f"Computer's hand: {computer_hand} | total: {sum(computer_hand)}")
    while len(computer_hand) != 5 and sum(computer_hand) < 17:
        computer_hand = add_card(computer_hand, cards)
        computer_hand = convert_aces(computer_hand)
        time.sleep(1)
        print(f"Computer's hand: {computer_hand} | total: {sum(computer_hand)}")

    # when the computer has less than 21 (not gone bust and no blackjack)
    # and does not have five cards in their deck
    # if they have a lower total than the player, and the player has not gone bust,
    # draw another card
    while sum(computer_hand) < 21 and len(computer_hand) != 5 and not bust(player_hand) and sum(computer_hand) < sum(player_hand):
        computer_hand = add_card(computer_hand, cards)
        computer_hand = convert_aces(computer_hand)
        time.sleep(1)
        print(f"Computer's hand: {computer_hand} | total: {sum(computer_hand)}")
    # display the result of the game
    time.sleep(2)
    if is_game_drawn(player_hand, computer_hand):
        pass
    else:
        has_user_won(player_hand, computer_hand)
    # ask the user if they wish to play again
    if play_again():
        main()


def play_again():
    time.sleep(1)
    answer = input("\nWould you like to play again (yes or no)?: ").lower()
    if answer != "yes" and answer != "no":
        print("Invalid option, ending game. Thank you for playing! \n")
        quit()
    elif answer == "yes":
        print()
        return True
    elif answer == "no":
        print("Thank you for playing! \n")
        quit()


def is_game_drawn(player, computer):
    if bust(player) and bust(computer):
        print(f"Player hand: {sum(player)} | Computer hand: {sum(computer)}")
        print("Draw! Both of you have gone bust!")
        return True
    elif sum(player) == sum(computer):
        print(f"Player hand: {sum(player)} | Computer hand: {sum(computer)}")
        print(f"Draw!")
        return True
    else:
        return False


def has_user_won(player, computer):
    if bust(computer):
        print(f"Player hand: {sum(player)} | Computer hand: {sum(computer)}")
        time.sleep(1)
        print("You win! Computer has gone Bust!")
        return True
    elif bust(player):
        print(f"Player hand: {sum(player)} | Computer hand: {sum(computer)}")
        time.sleep(1)
        print("You lose! Computer didn't go Bust!")
        return False
    elif sum(player) > sum(computer):
        print(f"Player hand: {sum(player)} | Computer hand: {sum(computer)}")
        time.sleep(1)
        print("You win! You have the higher score")
        return True
    elif sum(computer) > sum(player):
        if black_jack(computer):
            print(f"Player hand: {sum(player)} | Computer hand: {sum(computer)}")
            time.sleep(1)
            print("You lose! Computer wins via BLACKJACK!")
            return False
        else:
            print(f"Player hand: {sum(player)} | Computer hand: {sum(computer)}")
            time.sleep(1)
            print("You lose! Computer has the higher score!")
            return False


def add_card(hand, cards):
    hand.append(choice(cards))
    return hand


def hit(answer):
    while answer != "hit" and answer != "stand":
        answer = input("Not a valid option - please choose hit or stand: ").lower()
    if answer == "hit":
        return True
    elif answer == "stand":
        return False


def black_jack(hand):
    if sum(hand) == 21:
        return True
    else:
        return False


def display_hands(player, comp):
    hidden_cards = "[_]" * (len(comp) - 1)
    print(f"Computer's hand: {comp[0]} {hidden_cards}")
    print(f"Your hand: ", end="")
    for i in range(len(player)):
        print(f"{player[i]} ", end="")


def starting_cards(cards):
    player, computer = [], []
    for times in range(2):
        player.append(choice(cards))
        computer.append(choice(cards))
    return player, computer


def convert_aces(hand):
    if bust(hand):
        for index in range(len(hand)):
            if hand[index] == 11:
                hand[index] = 1
                if not bust(hand):
                    return hand
    return hand


def bust(hand):
    if sum(hand) > 21:
        return True
    else:
        return False


main()
