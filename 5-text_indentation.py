#!/usr/bin/python3
"""Module for text_indentation.

Provides a function that prints text with 2 new lines
after each '.', '?' and ':'.
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip(" ")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
