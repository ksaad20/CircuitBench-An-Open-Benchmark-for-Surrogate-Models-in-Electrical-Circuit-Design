"""
Input/output tests.
"""

import json
from pathlib import Path


def test_json_example():

    sample = {"circuit": "OpAmp", "gain": 10}

    text = json.dumps(sample)

    recovered = json.loads(text)

    assert recovered["gain"] == 10


def test_path_creation():

    p = Path("datasets")

    assert p.exists()
