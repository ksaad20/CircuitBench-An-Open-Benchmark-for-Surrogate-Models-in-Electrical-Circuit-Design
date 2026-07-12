"""
Metadata validation.
"""

from pathlib import Path

FILES = [
    "datasets.yaml",
    "contributors.yaml",
    "keywords.yaml",
    "publications.yaml",
]


def validate_metadata(root="datasets/metadata"):

    root = Path(root)

    errors = []

    for file in FILES:
        if not (root / file).exists():
            errors.append(file)

    if errors:
        print("Missing metadata files:")
        for f in errors:
            print(f" - {f}")
        return False

    print("Metadata validation passed.")
    return True


if __name__ == "__main__":
    validate_metadata()
