"""
Module responsible for improving strings.
"""

from random import choice

from owoify.owoify import Owoness, owoify
from owoify.utility.mapping import FACES
from unidecode import unidecode


def uwuify(input: str) -> str:
    """
    Improve given strings with `owoify.owoify.owoify`

    First all non-ASCII characters are removed.
    Then resulting text is send through `owoify.owoify.owoify` with maximum `owoify.owoify.Owoness`.
    Additionally, two `owoify.utility.mapping.FACES` are added surrounding resulting text.
    """
    normalized_input = unidecode(input)
    return f"{choice(FACES)} {owoify(normalized_input, Owoness.Uvu)} {choice(FACES)}"
