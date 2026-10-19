#!/usr/bin/env python3
"""Calculate the correlation matrix from a covariance matrix."""

import numpy as np


def correlation(C):
    """Calculate the correlation matrix of a covariance matrix."""
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    d = C.shape[0]
    std = np.sqrt(np.diag(C))
    corr = C / np.outer(std, std)

    return corr
