"""
Reproducibility utilities.
"""

import random
import numpy as np


def set_seed(seed=42):

    random.seed(seed)

    np.random.seed(seed)

    try:
        import torch

        torch.manual_seed(seed)

        torch.cuda.manual_seed_all(seed)

    except Exception:

        pass
