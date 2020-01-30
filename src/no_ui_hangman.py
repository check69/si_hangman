import random
from msvcrt import getch
import os
from typing import List
from re import finditer

WORD_LIST = ("python", "sports", "interactive")

MAX_LIVES = 7


HEAD = ""
BODY = ""
RIGHT_ARM = ""
LEFT_ARM = " "
ABS = ""
RIGHT_LEG = ""
LEFT_LEG = ""


def paint_hangman():
    global HEAD
    global BODY
    global LEFT_ARM
    global RIGHT_ARM
    global ABS
    global LEFT_LEG
    global RIGHT_LEG
    HANGMAN_DRAW = ("_________",
                    "|       |",
                    f"|       {HEAD}",
                    f"|      {LEFT_ARM}{BODY}{RIGHT_ARM}",
                    f"|       {ABS}",
                    f"|      {LEFT_LEG} {RIGHT_LEG}",
                    "|_________")
    for i in HANGMAN_DRAW:
        print(i)


def get_word() -> str:
    return WORD_LIST[random.randint(0, len(WORD_LIST) - 1)]


def paint_letters(guessed: List[str]):
    print(" ".join(guessed))


def find_all_elements(word: str, letter: str) -> List[int]:
    pos = []
    for i in range(len(word)):
        if word[i] == letter:
            pos.append(i)
    return pos


def victory(guessed: List[str], word: str):
    return "".join(guessed) == word


def lost_life(lives: int):
    lives -= 1
    if lives == 6:
        global HEAD
        HEAD = "O"
    if lives == 5:
        global BODY
        BODY = "|"
    if lives == 4:
        global LEFT_ARM
        LEFT_ARM = "\\"
    if lives == 3:
        global RIGHT_ARM
        RIGHT_ARM = "/"
    if lives == 2:
        global ABS
        ABS = "|"
    if lives == 1:
        global LEFT_LEG
        LEFT_LEG = "/"
    if lives == 0:
        global RIGHT_LEG
        RIGHT_LEG = "\\"

    return lives


def main():
    word = get_word()
    lives = MAX_LIVES
    guessed = ["_"]*len(word)

    while lives > 0:
        paint_letters(guessed)
        paint_hangman()
        key = getch()
        key = str(key.lower(), "utf-8")
        if not key.isalpha():
            lost_life(lives)
        else:
            positions = find_all_elements(word, key)
            if not positions:
                lives = lost_life(lives)
            else:
                for i in positions:
                    guessed[i] = key

        if victory(guessed, word):
            print("You WIN!!!!")
            paint_letters(guessed)
            exit(0)

        os.system('cls')

    paint_letters(guessed)
    paint_hangman()
    print("You LOSE!!!!")


if __name__ == "__main__":
    main()
