from discord.utils import escape_markdown, remove_markdown

from uwuifier import uwuify


def prepare_text(text: str) -> str:
    trimmed_text = remove_markdown(text)
    uwuified_text = uwuify(trimmed_text)
    return escape_markdown(uwuified_text)
