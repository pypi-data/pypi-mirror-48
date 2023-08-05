import bisect
import collections
import math


def find_index(seq, val):
    """Assume ``seq`` is sorted and search for the position of ``val``."""
    i = bisect.bisect_left(seq, val)
    if i != len(seq) and seq[i] == val:
        return i
    raise ValueError(f'{val} was not found')


def is_in(seq, val):
    """Assume ``seq`` is sorted and check if it contains ``val``."""
    i = bisect.bisect_left(seq, val)
    return i < len(seq) and seq[i] == val


class Histogram(collections.Counter):
    """Streaming histogram data structure.

    Parameters:
        max_bins (int): Maximal number of bins.

    Attributes:
        n_bins (int): Current number of bins.
        sorted_bins (list): Sorted left bin values.

    Example:

        ::

            >>> from creme import utils
            >>> import matplotlib.pyplot as plt
            >>> import numpy as np

            >>> np.random.seed(42)

            >>> values = np.hstack((
            ...     np.random.normal(-3, 1, 1000),
            ...     np.random.normal(3, 1, 1000),
            ... ))

            >>> hist = utils.Histogram(max_bins=12)

            >>> for x in values:
            ...     hist = hist.update(x)

            >>> print(hist)
            [-5.53514, -4.55869): 9
            [-4.55869, -3.61492): 94
            [-3.61492, -2.58699): 338
            [-2.58699, -1.44212): 423
            [-1.44212, -0.12576): 128
            [-0.12576, 0.98003): 13
            [0.98003, 1.81977): 31
            [1.81977, 2.69824): 150
            [2.69824, 3.57935): 339
            [3.57935, 4.58907): 329
            [4.58907, 5.89119): 142

            >>> ax = plt.bar(hist.keys(), hist.values())

        .. image:: ../_static/histogram_docstring.svg
            :align: center

    References:
        1. `A Streaming Parallel Decision Tree Algorithm <http://jmlr.org/papers/volume11/ben-haim10a/ben-haim10a.pdf>`_
        2. `Streaming Approximate Histograms in Go <https://www.vividcortex.com/blog/2013/07/08/streaming-approximate-histograms/>`_
        3. `Go implementation <https://github.com/VividCortex/gohistogram>`_

    """

    def __init__(self, max_bins=256):
        self.sorted_bins = []
        self.max_bins = max_bins

    @property
    def n_bins(self):
        return len(self)

    def update(self, x):

        super().update([x])

        # Update the sorted list of bin values
        if not is_in(self.sorted_bins, x):
            bisect.insort_left(self.sorted_bins, x)

        # Bins have to be merged if there are more than max_bins
        while self.n_bins > self.max_bins:

            # Find the nearest bins
            min_val = math.inf
            min_idx = None

            # TODO: this loop should be Cythonized
            for i, (a, b) in enumerate(zip(self.sorted_bins[:-1], self.sorted_bins[1:])):
                if b - a < min_val:
                    min_val = b - a
                    min_idx = i

            left_bin = self.sorted_bins[min_idx]
            right_bin = self.sorted_bins[min_idx + 1]

            # Merge the two bins by summing their count and making a weighted average for each one
            total_count = self[left_bin] + self[right_bin]
            new_bin = left_bin * self[left_bin] + right_bin * self[right_bin]
            new_bin /= total_count

            bisect.insort_left(self.sorted_bins, new_bin)

            # Deletion of the two bins to replace them with the new one resulting from their merging
            for k in [left_bin, right_bin]:
                self.pop(k, None)
                self.sorted_bins.pop((find_index(self.sorted_bins, k)))

            super().update({new_bin: total_count})

        return self

    def bin(self, x):
        """Returns the number of the bin where ``x`` belongs."""
        return bisect.bisect_left(self.sorted_bins, x)

    def __str__(self):

        if len(self) == 1:
            return f'{self.sorted_bins[0]:.5f}: {self[self.sorted_bins[0]]}'

        return '\n'.join(
            f'[{a:.5f}, {b:.5f}): {self[a]}'
            for a, b in zip(self.sorted_bins[:-1], self.sorted_bins[1:])
        )
