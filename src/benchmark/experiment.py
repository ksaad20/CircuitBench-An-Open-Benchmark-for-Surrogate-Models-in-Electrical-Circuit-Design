"""
CircuitBench Experiment Manager
===============================

Central experiment object responsible for reproducibility,
tracking, metadata, timing and result storage.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import json
import platform
import sys
import time
import uuid
from datetime import datetime
from pathlib import Path


class Experiment:
    """
    Reproducible benchmark experiment.
    """

    def __init__(self, name: str, description: str = ""):

        self.id = str(uuid.uuid4())

        self.name = name

        self.description = description

        self.created = datetime.utcnow().isoformat()

        self.models = []

        self.datasets = []

        self.metrics = {}

        self.parameters = {}

        self.results = []

        self.tags = []

        self.seed = None

        self.elapsed = None

        self.notes = ""

    # ---------------------------------------------------------

    def add_model(self, model):

        self.models.append(model)

    # ---------------------------------------------------------

    def add_dataset(self, dataset):

        self.datasets.append(dataset)

    # ---------------------------------------------------------

    def add_metric(self, name, value):

        self.metrics[name] = value

    # ---------------------------------------------------------

    def add_result(self, result):

        self.results.append(result)

    # ---------------------------------------------------------

    def set_seed(self, seed):

        self.seed = seed

    # ---------------------------------------------------------

    def set_parameters(self, **kwargs):

        self.parameters.update(kwargs)

    # ---------------------------------------------------------

    def add_tag(self, tag):

        if tag not in self.tags:
            self.tags.append(tag)

    # ---------------------------------------------------------

    def start(self):

        self._start = time.perf_counter()

    # ---------------------------------------------------------

    def stop(self):

        self.elapsed = time.perf_counter() - self._start

    # ---------------------------------------------------------

    def system_information(self):

        return {
            "python": sys.version,
            "platform": platform.platform(),
            "processor": platform.processor(),
            "machine": platform.machine(),
        }

    # ---------------------------------------------------------

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created": self.created,
            "models": self.models,
            "datasets": self.datasets,
            "metrics": self.metrics,
            "parameters": self.parameters,
            "results": self.results,
            "tags": self.tags,
            "seed": self.seed,
            "elapsed": self.elapsed,
            "system": self.system_information(),
        }

    # ---------------------------------------------------------

    def save(self, directory="experiments"):

        directory = Path(directory)

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        file = directory / f"{self.id}.json"

        with open(file, "w", encoding="utf-8") as f:
            json.dump(
                self.to_dict(),
                f,
                indent=4,
            )

        return file

    # ---------------------------------------------------------

    @classmethod
    def load(cls, file):

        with open(file, encoding="utf-8") as f:
            return json.load(f)

    # ---------------------------------------------------------

    def summary(self):

        print("=" * 70)

        print("CircuitBench Experiment")

        print("=" * 70)

        print(f"ID          : {self.id}")

        print(f"Name        : {self.name}")

        print(f"Models      : {len(self.models)}")

        print(f"Datasets    : {len(self.datasets)}")

        print(f"Metrics     : {len(self.metrics)}")

        print(f"Results     : {len(self.results)}")

        print(f"Elapsed     : {self.elapsed}")

        print("=" * 70)
