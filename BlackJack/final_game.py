from deck_class import Deck
from hand_class import Hand
from chips_class import Chips

playing = True


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("Enter the bet value in numbers : "))
        except:
            print("Invalid input value for the bet")
        else:
            if chips.bet > chips.total or chips.bet == 0:
                print("Sorry, your bet can't exceed or bet with 0", chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s : ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player Stands, Dealers turn !")
            playing = False
        else:
            print("I dont understand, Please enter h or s only!")
            continue
        break


def show_some(player, dealer):

    print('\n Dealers hand: ')
    print("First card hidden!")
    print(dealer.cards[1])

    print('\n Players hand: ')
    for card in player.cards:
        print(card)


def show_all(player, dealer):

    print('\n Dealers hand: ', *dealer.cards, sep='\n')

    print("Value of Dealers hand is: {} ".format(dealer.value))

    print('\n Players hand: ')
    for card in player.cards:
        print(card)

    print("Value of Players hand is: {} ".format(player.value))


def player_busts(player, dealer, chips):
    print("Player BUSTED")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player WINS")
    chips.win_bet()
    pass


def dealer_busts(player, dealer, chips):
    print("Player WINS, Dealer BUSTED!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer WINS!")
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and player tie! PUSH!!')


if __name__ == '__main__':

    # Placing the chips assigning outside the while loop in order to avoid the resetting on players chips status
    player_chips = Chips()

    while True:
        # Print an opening statement
        print("Welcome to Batcha's BLACKJACK")

        # First setting up the Deck to start the game play !
        deck = Deck()
        deck.shuffle_deck()

        # Second, creating the hand for the player and the Dealer

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Prompt the Player for their bet
        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand. value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value == player_hand.value:
                push(player_hand, dealer_hand)

        # Inform Player of their chips total
        print('\n Players total chips are at {}'. format(player_chips.total))

        if player_chips.total == 0:
            print("Thank you playing !!")
            break

        # Ask to play again
        new_game = input("Would you like to play another hand? Y/N : ")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            playing = False
            print("Thank you playing !!")
            break
