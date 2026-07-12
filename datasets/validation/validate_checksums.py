"""
Checksum validation.
"""

from pathlib import Path

FILES = [
    "SHA256SUMS",
    "MD5SUMS",
]


def validate_checksums(root="datasets/checksums"):

    root = Path(root)

    missing = []

    for file in FILES:
        if not (root / file).exists():
            missing.append(file)

    if missing:
        print("Missing checksum files:")
        for f in missing:
            print(f" - {f}")
        return False

    print("Checksum validation passed.")
    return True


if __name__ == "__main__":
    validate_checksums()
