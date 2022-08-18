"""
Module responsible for "improving" text.
First any markdown characters are removed.
Then text is uwuified.
Finally all markdown characters are escaped.
Some faces contain markdown characters, so the final step is necessary.
"""

from disnake.utils import escape_markdown, remove_markdown

from uwuifier import uwuify


def prepare_text(text: str) -> str:
    trimmed_text = remove_markdown(text)
    uwuified_text = uwuify(trimmed_text)
    return escape_markdown(uwuified_text)
