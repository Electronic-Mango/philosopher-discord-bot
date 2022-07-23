from random import choice

from owoify.owoify import owoify, Owoness
from owoify.utility.mapping import FACES
from unidecode import unidecode


def uwuify(input: str) -> str:
    normalized_input = unidecode(input)
    return f"{choice(FACES)} {owoify(normalized_input, Owoness.Uvu)} {choice(FACES)}"
