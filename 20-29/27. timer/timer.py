from contextlib import ContextDecorator
from statistics import mean, median
from time import time


class Timer(ContextDecorator):
    def __init__(self, func=None):
        self.runs = []
        self.func = func

    @property
    def elapsed(self):
        return self.runs[-1] if self.runs else None

    @property
    def min(self):
        return min(self.runs)

    @property
    def max(self):
        return max(self.runs)

    @property
    def mean(self):
        return mean(self.runs)

    @property
    def median(self):
        return median(self.runs)

    def __enter__(self):
        self.t = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.runs.append(time() - self.t)

    def __call__(self, *args, **kwargs):
        t = time()
        ret_var = self.func(*args, **kwargs)
        self.runs.append(time() - t)
        return ret_var
