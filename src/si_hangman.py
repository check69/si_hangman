import random
from typing import List
from re import finditer

word_list = ['train', 'crisp', 'tacos', 'click', 'words', 'euros', 'trite', 'fluff', 'power']


def get_word():
    return word_list[random.randint(0, len(word_list) - 1)]


def make_guess(word: str, letter: str) -> bool:
    if letter in word:
        return True

    return False


def find_all_elements(word: str, letter: str) -> List[int]:
    return [m.start() for m in finditer(letter, word)]
