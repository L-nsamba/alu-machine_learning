#!/usr/bin/env python3
"""Calculate posterior probabilities using Bayes' theorem."""

import numpy as np


def posterior(x, n, P, Pr):
    """Calculate posterior probabilities for hypothetical probabilities."""
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

    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError(
            "Pr must be a numpy.ndarray with the same shape as P"
        )

    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    if np.any((Pr < 0) | (Pr > 1)):
        raise ValueError("All values in Pr must be in the range [0, 1]")

    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    intersection_values = __import__(
        'intersection'
    ).intersection(x, n, P, Pr)

    marginal_value = np.sum(intersection_values)

    return intersection_values / marginal_value
