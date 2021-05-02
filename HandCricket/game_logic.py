from player_class import Player
import random
import time

# Dictionary to display the runs in a readable format
runs = {0: 'Dot', 1: 'Single', 2: 'Double', 3: 'Three', 4: 'Boundary', 5: 'Five', 6: 'Six'}


def toss():
    '''
    To randomly simulate the toss
    '''
    return random.randint(0, 1)


def play(player, opponent):
    wicket = False
    while not wicket:
        run = random.randint(0, 6)
        #run = int(input("Choose a number from 0 to 6 ==> "))
        if run == random.randint(0, 6):
            wicket = True
            player.wicket = True
            print(f"Its WICKET!!! {player.name} got out.. Total score is {player.score}")
            if player.wicket == opponent.wicket:
                if player.check_if_win() == 'No':
                    print(f"{opponent.name} won the match!")
                    return False

            opponent.target = player.score
            opponent.play = True

            print("Target is {}".format(opponent.target))
            return True
        else:
            player.add_score(run)
            time.sleep(1)
            print(f"{player.name} scored: {runs.get(run)}")
            if opponent.wicket:
                if player.check_if_win() == "Yes":
                    print(f"{player.name} won the match! Total score is {player.score}")
                    return False
                elif player.check_if_win() == "Tie":
                    print("Match Tied!")
                    return False


if __name__ == "__main__":
    print("Welcome to the Batcha's Handcricket Tournament !!")

    while True:
        player1 = Player("Batcha")
        player2 = Player("Computer")

        if toss():
            player1.play = True
        else:
            player2.play = True

        game_on = True
        print("The game is going to start in a minute..")
        while game_on:

            if player1.play and not player1.wicket:
                print(f"{player1.name} is going to Bat")
                game_on = play(player1, player2)
                continue

            elif player2.play and not player2.wicket:
                print(f"{player2.name} is going to Bat")
                game_on = play(player2, player1)
                continue

        replay = input("Press Y if you want to play again: ")
        if replay.lower() == "y":
            continue
        else:
            break
