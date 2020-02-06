import random
from typing import List
from utils import clear_screen
from utils import get_key
from utils import get_random_number

WORD_LIST = ("python", "sports", "interactive")

MAX_LIVES = 7


HANGMAN = ["_________",
           "|       |",
           "| ",
           "|",
           "|",
           "|",
           "|_________"
           ]

matches = {
    6: (2, "|       O"),
    5: (3, "|       |"),
    4: (3, "|      \\|"),
    3: (3, "|      \\|/"),
    2: (4, "|       |"),
    1: (5, "|      /"),
    0: (5, "|      / \\"),
}


def paint_hangman():
    for i in HANGMAN:
        print(i)


def get_word() -> str:
    return WORD_LIST[get_random_number(0, len(WORD_LIST) - 1)]


def paint_letters(guessed: List[str]):
    print(" ".join(guessed))


def find_all_elements(word: str, letter: str) -> List[int]:
    return [pos for pos in range(len(word)) if word[pos] == letter]


def victory(guessed: List[str], word: str):
    return "".join(guessed) == word


def lost_life(lives: int):
    lives -= 1
    i, v = matches.get(lives)
    HANGMAN[i] = v
    return lives


def paint(guessed: List[str]):
    paint_letters(guessed)
    paint_hangman()


def update(word: str, lives: int, guessed: List[str]) -> int:
    paint(guessed)
    key = get_key()
    if key.isalpha():
        positions = find_all_elements(word, key)
        if not positions:
            lives = lost_life(lives)
        else:
            for i in positions:
                guessed[i] = key

    clear_screen()

    return lives


def end_game(word: str, lives: int, guessed: List[str]):
    if victory(guessed, word):
        print("You WIN!!!!")
    else:
        print("You LOSE!!!!")
    paint(guessed)


def init():
    word = get_word()
    return word, MAX_LIVES, ["_"]*len(word)


def main():
    word, lives, guessed = init()

    while lives > 0:
        lives = update(word, lives, guessed)
        if victory(guessed, word):
            break

    end_game(word, lives, guessed)


if __name__ == "__main__":
    main()
