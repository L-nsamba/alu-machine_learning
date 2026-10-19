#!/usr/bin/env python3
"""Calculate the likelihood of binomial observations."""

import numpy as np


def likelihood(x, n, P):
    """Calculate binomial likelihoods for a range of probabilities."""
    if not isinstance(n, (int, np.integer)) or isinstance(n, (bool, np.bool_)) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, (int, np.integer)) or isinstance(x, (bool, np.bool_)) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    coeff = 1
    for i in range(1, min(x, n - x) + 1):
        coeff = coeff * (n - i + 1) // i

    return coeff * (P ** x) * ((1 - P) ** (n - x))
