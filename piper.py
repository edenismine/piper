#!/usr/bin/env python3
import pathlib
import click
import re

#: Default prompt
PROMPT = ': '

#: Introduction text
INTRO = '''This utility will walk you through creating a setup.py file.
It only covers the most common items, and tries to guess sensible defaults.'''


def get_valid_string(regex: str, message: str, flags: int = 0) -> str:
    """Gets a valid string from the user, given a regex pattern and a message

    :param regex:   Regular expression the string should match.
    :param message: The message used to prompt the user for input.
    :param flags:   **re** module flags.
    :returns: A valid user-provided string that matches the regex.
    """
    result = ""
    visited = False
    while not match(regex, result, flags):
        if visited:
            message = f'{Deco.WARNING}Invalid input, please try ' \
                      f'again{Deco.END}\n{PROMPT}'
        result = input(message).strip()
        visited = True
    return result


def match(regex: str, string: str, flags: int = 0) -> bool:
    """Checks if a string matches a regex pattern."""
    return bool(re.match(regex.encode('utf-8'), string.encode('utf-8'), flags))


class Deco:
    """Terminal decorators adapted from https://stackoverflow.com/a/287944"""
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


@click.command()
def cli():
    """Entry point for the application script"""
    # TODO Read config in ~/.piper
    # config.author
    # config.author_email

    # TODO introduce the scripts functionality:
    # TODO Ask package name, default to parent directory's name
    # Package names regex: ^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$

    # TODO Ask version, default to 0.1.0

    # TODO Ask for description

    # TODO Ask for git repository url

    # TODO Ask for author, default to current user or config.author

    # TODO Ask for author_email, default to config.author_email

    # TODO Ask for license template default to MIT

    # TODO Confirm setup:
    # About to write to {parent_directory}/setup.py

    # TODO Create README.rst with description.

    # TODO Create Manifest.in to include README.rst

    # TODO Create base file structure
    # pathlib.Path(f'/{package_name}/{package_name}').mkdir(
    #     parents=True, exist_ok=True)
    print("Call your main application code here")
