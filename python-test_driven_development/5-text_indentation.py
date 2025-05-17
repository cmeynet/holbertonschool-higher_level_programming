#!/usr/bin/python3
"""
This is the "5-text_indentation" module
It coutains the function:
text_indentation
"""


def text_indentation(text):
    """ Print a text with 2 new lines after ".", "?", and ":"
    with no leading/trailing spaces.

    Args:
        text: text to print

    Returns:
        The text with 2 new lines after ".", "?", ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""  # Accumulates characters in a line
    for char in text:
        line += char
        if char in ".:?":
            # Removes spaces at the beginning/end of a line
            print(line.strip())
            print()
            line = ""  # Reset to start a new line

    # Display the rest of the text if it doesn't end with punctuation
    if line.strip():
        print(line.strip(), end="")
