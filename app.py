
import os
from turtle import color
from termcolor import colored

from BeetleVisualiser import draw_beetle, BeetleParts

import random

from time import sleep


def prompt_main_menu():

    print(colored(
        """
Please choose from the following:
=================================
1. Roll the dice.
2. Visualise your beetle.
3. Visualise computer's beetle.
        """, "cyan"))

    response = input("> ")
    if len(response) == 0:
        print(colored("Please submit a response.", "red"))
        return prompt_main_menu()

    try:
        responseInt = int(response)
    except:
        print(colored("Please enter a number from the options.", "red"))
        return prompt_main_menu()

    return responseInt


def process_dice_result(result):
    # return [Bool, BeetlePart]
    qualifyingParts = DICE_THROW_RESULTS[str(result)]

    if turnToPlay == "COMPUTER":
        stats = computerStats

    if turnToPlay == "PLAYER":
        stats = playerStats

    if result != 6:
        if BeetleParts.BODY not in stats['beetleParts']:
            return [False, None]

    if result == 2 or result == 3:
        if BeetleParts.HEAD not in stats['beetleParts']:
            return [False, None]

    for qualifyingPart in qualifyingParts:
        if qualifyingPart not in stats['beetleParts']:
            partToAppend = qualifyingPart
        else:
            partToAppend = None
            continue

    if partToAppend == None:
        return [False, partToAppend]
    else:
        stats['beetleParts'].append(partToAppend)
        return [True, partToAppend]


def computer_turn_to_play():
    os.system("cls")
    print(colored("Computer is rolling dice...", "grey"))
    diceResult = roll_dice()
    processResult = process_dice_result(diceResult)
    sleep(2)
    print(colored(f"Computer rolled a {diceResult}!", "yellow"))
    if processResult[0] == True:
        print(colored(F"It drew a {processResult[1]['key']}.", "yellow"))
    else:
        print(colored("Nothing new has been drawn.", "yellow"))


def player_turn_to_play():
    os.system("cls")
    mainMenuResponse = prompt_main_menu()
    if mainMenuResponse == 1:
        print(colored("Rolling dice...", "grey"))
        diceResult = roll_dice()
        processResult = process_dice_result(diceResult)

        sleep(2)
        print(colored(f"You rolled a {diceResult}!", "yellow"))
        if processResult[0] == True:
            print(colored(F"You drew a {processResult[1]['key']}."))
        else:
            print(colored("Nothing new has been drawn.", "yellow"))

    elif mainMenuResponse == 2:
        draw_beetle(playerStats["beetleParts"], "Player Beetle")
        return player_turn_to_play()
    else:

        draw_beetle(computerStats["beetleParts"], "Computer Beetle")
        return player_turn_to_play()


def StartGame():
    global turnToPlay
    if turnToPlay == "PLAYER":
        player_turn_to_play()
        turnToPlay = "COMPUTER"
    else:
        computer_turn_to_play()
        turnToPlay = "PLAYER"

    if len(playerStats["beetleParts"]) == 13:
        print(
            colored("Congratulations! You won!\nRelaunch this app to play again.", "green"))
        return

    if len(computerStats["beetleParts"]) == 13:
        print(
            colored("Oh no! Unfortunately, you lost.\nRelaunch this app to play again.", "red"))
        return

    sleep(5)
    StartGame()


def roll_dice():
    return random.randint(1, 6)


def main():
    os.system("color")

    print(colored("Welcome!\nReady to play? Press ENTER to begin.", "cyan"))
    input()

    StartGame()


if __name__ == "__main__":
    DICE_THROW_RESULTS = {
        "6": [BeetleParts.BODY],
        "5": [BeetleParts.HEAD],
        "4": [BeetleParts.LEFT_LEG_TOP, BeetleParts.LEFT_LEG_MIDDLE, BeetleParts.LEFT_LEG_BOTTOM, BeetleParts.RIGHT_LEG_TOP, BeetleParts.RIGHT_LEG_MIDDLE, BeetleParts.RIGHT_LEG_BOTTOM],
        "3": [BeetleParts.LEFT_EYE, BeetleParts.RIGHT_EYE],
        "2": [BeetleParts.LEFT_ANTENNA, BeetleParts.RIGHT_ANTENNA],
        "1": [BeetleParts.TAIL]
    }
    playerStats = {"beetleParts": [BeetleParts.BODY, BeetleParts.HEAD, BeetleParts.LEFT_LEG_TOP, BeetleParts.LEFT_LEG_MIDDLE, BeetleParts.LEFT_LEG_BOTTOM, BeetleParts.RIGHT_LEG_TOP,
                                   BeetleParts.RIGHT_LEG_MIDDLE, BeetleParts.RIGHT_LEG_BOTTOM, BeetleParts.LEFT_EYE, BeetleParts.RIGHT_EYE, BeetleParts.LEFT_ANTENNA, BeetleParts.RIGHT_ANTENNA]}
    computerStats = {"beetleParts": []}
    turnToPlay = "COMPUTER"
    main()
