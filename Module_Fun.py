import random
from pathlib import Path


def dice_roll():
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    return first, second


def choose_leader(names):
    leader = random.choice(names)
    return leader


def file_operations(filename):
    files = []
    path = Path()
    for file in path.glob(filename):
        files.append(file)
    return files
