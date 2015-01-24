#!/usr/local/bin/python3
""" Week 3 homework, blackjack problem """
# 2015-01-23
# Joseph Urbanski
# MPCS 50101

# PLEASE NOTE:  The base mandatory requirements for this assignment were
# contradictory or nonsensical IMHO, so I created something closer to a real
# game as included in the optional/bonus requirements.  I however will always
# treat an ace as an eleven, ignoring optional requirement #1.

import random
import time

# Deck constants.
# PLEASE NOTE: Unlike Prof. Cohen's example, I'm using a 'T' instead of '10'
# to represent a ten.  That allows me to always have two character pairs for
# the cards in my deck.
SUITS = "\u2663 \u2665 \u2666 \u2660".split()
FACES = "A 2 3 4 5 6 7 8 9 T J Q K".split()

def initialize_deck():
    """ Will create and shuffle a deck of cards. """
    deck = []
    for suit in SUITS:
        for face in FACES:
            deck.append(face+suit)
    random.shuffle(deck)
    return deck

def print_hand(hand):
    """ Prints the hand with spaces between cards. """
    i = 0
    while i < len(hand):
        # If it's a 'T', print out '10'
        if hand[i] == 'T':
            print("10", end='')
        # If it's not a suit, just print it out
        elif ord(hand[i]) < 128:
            print(hand[i], end='')
        # Otherwise, it's a suit, so print it out with a space afterwards
        else:
            print(hand[i], end=' ')
        i += 1
    print()

def print_player_hand(hand):
    """ Neatly prints the player's hand. """
    print("Player's hand:")
    print_hand(hand)

def print_cpu_hand(hand):
    """ Neatly prints out the dealer's hand. """
    print("Dealer's hand:")
    print_hand(hand)

def print_cpu_hand_mask_first_card(hand):
    """ Masks the first card, then neatly prints rest of the dealer's hand. """
    print("Dealer's hand:")
    print("??", end=' ')
    print_hand(hand[2:])

def eval_hand(hand):
    """ Totals points in a given hand. """
    i = 0
    total = 0
    while i < len(hand) - 1:
        # If it's a not a face card or a ten, just add the value of the card.
        try:
            total += int(hand[i])
        # Otherwise, add 11 for an ace, and 10 for face cards and ten cards.
        except ValueError:
            if hand[i] == 'A':
                total += 11
            else:
                total += 10
        i += 2
    return total

def main():
    """ Main function """
    deck = initialize_deck()

    # Deal the cards one at a time, starting with the player, until both
    # players have two cards.
    player_hand = deck.pop()
    cpu_hand = deck.pop()
    player_hand += deck.pop()
    cpu_hand += deck.pop()

    print_player_hand(player_hand)

    # Check to see if the player blackjacks.
    if eval_hand(player_hand) == 21:
        print_cpu_hand(cpu_hand)
        print("BLACKJACK! You win!")
        return

    # Check to see if the dealer blackjacks.
    if eval_hand(cpu_hand) == 21:
        print_hand(cpu_hand)
        print("BLACKJACK! You lose!")
        return

    # Hide the dealer's first card until the player has finished his turn.
    print_cpu_hand_mask_first_card(cpu_hand)

    # Prompt the player for another card, checking for a bust or 21 after
    # the draw.
    while bool(input("Would you like another card? (Hit \'Enter\' to hold):")):
        player_hand += deck.pop()
        print_player_hand(player_hand)
        if eval_hand(player_hand) > 21:
            print("BUST! You lose!")
            break
        if eval_hand(player_hand) == 21:
            print("TWENTY-ONE!")
            break

    # Now that the player has finished his turn, it's okay to reveal the
    # dealer's cards.
    print_cpu_hand(cpu_hand)

    # If the player has busted then exit this function and end the game.
    if eval_hand(player_hand) > 21:
        return

    # Have the dealer keep drawing cards until they have 17 or more points.
    while eval_hand(cpu_hand) < 17:
        time.sleep(4)
        cpu_hand += deck.pop()
        print_cpu_hand(cpu_hand)

    if eval_hand(cpu_hand) > 21:                        # Dealer bust
        print("DEALER BUSTS! You win!")
    elif eval_hand(player_hand) == eval_hand(cpu_hand): # Tie game
        print("PUSH! Players tie.")
    elif eval_hand(player_hand) > eval_hand(cpu_hand):  # Player wins
        print("You win!")
    else:
        print("You lose!")                              # Player loses

main()

# Prompt for another game.
while bool(input("Would you like to play again? (Hit \'Enter\' to quit):")):
    main()
