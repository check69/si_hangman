import random
from typing import List
from re import finditer
from utils import get_random_number

WORD_LIST = ['python', 'sports', 'train', 'crisp', 'tacos', 'click', 'words', 'euros', 'trite', 'fluff', 'power']


def get_word() -> str:
    return WORD_LIST[get_random_number(0, len(WORD_LIST) - 1)]


def make_guess(word: str, letter: str) -> bool:
    return letter in word


def find_all_elements(word: str, letter: str) -> List[int]:
    return [m.start() for m in finditer(letter, word)]
