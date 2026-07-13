"""
Shell completion helpers.
"""

from __future__ import annotations


def available_shells():
    return [
        "bash",
        "zsh",
        "fish",
        "powershell",
    ]


def install(shell: str):

    shell = shell.lower()

    if shell not in available_shells():
        raise ValueError(f"Unsupported shell: {shell}")

    print(f"Shell completion installation for {shell} is not yet implemented.")
