import sys
from math import ceil


class ProgressBar(object):
    """
    Display a progress bar which show the advancement of a process
    """

    def __init__(self, n, length=30):
        """
        Parameters
        ----------
        n: int
            Length of the iterative process
        length: int
            Number of characters of the progress bar
        """
        self._n = n
        self._length = length

    def advance(self, i):
        """
        Advance the progress bar to state i

        Parameters
        ----------
        i: int
            State of the process
        """
        sys.stdout.write('\r')
        sys.stdout.write("[%-30s] %d%%" % ('=' * int(
            ceil(i / self._n * self._length)),
            (i + 1) / self._n * 100))
        sys.stdout.flush()

    def close(self):
        """
        Close the progress bar
        """
        sys.stdout.write('\n')
