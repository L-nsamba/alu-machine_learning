#!/usr/bin/env python3
"""Define a class representing a multivariate normal distribution."""

import numpy as np


class MultiNormal:
    """Represent a multivariate normal distribution."""

    def __init__(self, data):
        """Initialize the distribution using a data set."""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)

        centered = data - self.mean
        self.cov = np.matmul(centered, centered.T) / (n - 1)

    def pdf(self, x):
        """Calculate the PDF at a given data point."""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]

        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        diff = x - self.mean
        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)

        norm = 1 / np.sqrt((2 * np.pi) ** d * det)
        exponent = -0.5 * np.matmul(
            np.matmul(diff.T, inv), diff
        )

        return float(norm * np.exp(exponent))
