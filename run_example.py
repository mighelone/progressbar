from scoop import futures

import time

from progressbar import ProgressBar


def f(i):
    time.sleep(0.02)


if __name__ == '__main__':
    n = 100
    results = futures.map(f, range(n))
    bar = ProgressBar(n)
    [bar.advance(i) for i, _ in enumerate(results)]
    bar.close()
