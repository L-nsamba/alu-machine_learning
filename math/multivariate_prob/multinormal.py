
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
