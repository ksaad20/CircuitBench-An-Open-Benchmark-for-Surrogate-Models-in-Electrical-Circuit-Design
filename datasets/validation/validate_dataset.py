"""
Dataset structure validation.
"""

from pathlib import Path

REQUIRED_DIRECTORIES = [
    "raw",
    "processed",
    "metadata",
    "schema",
    "statistics",
    "validation",
]


def validate_dataset(root="datasets"):
    root = Path(root)

    missing = []

    for directory in REQUIRED_DIRECTORIES:
        if not (root / directory).exists():
            missing.append(directory)

    if missing:
        print("Missing directories:")
        for d in missing:
            print(f" - {d}")
        return False

    print("Dataset structure validation passed.")
    return True


if __name__ == "__main__":
    validate_dataset()
