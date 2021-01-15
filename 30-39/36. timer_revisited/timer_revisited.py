from contextlib import ContextDecorator
from time import time


class Timer(ContextDecorator):

    named_timers = {}

    def __new__(cls, name=None):
        return cls.named_timers.get(name, super(Timer, cls).__new__(cls))

    def __init__(self, name=None):
        if not hasattr(self, 'running'):
            if name:
                self.__class__.named_timers[name] = self
            self.runs = []
            self.running = False
            self.sub_timers = []
            self.sub_timer_name_map = {}

    @property
    def elapsed(self):
        return self.runs[-1] if self.runs else None

    def __enter__(self):
        self.running = True
        self.t = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.running = False
        self.runs.append(time() - self.t)

    def __getitem__(self, item):
        if isinstance(item, int):
            idx = item
        elif isinstance(item, str):
            idx = self.sub_timer_name_map[item]
        else:
            raise NotImplementedError
        return self.sub_timers[idx]

    def split(self, name=None):
        if not self.running:
            raise RuntimeError('Cannot split because parent timer is not running')
        if name:
            if name in self.sub_timer_name_map:
                return self.sub_timers[self.sub_timer_name_map[name]]
            self.sub_timer_name_map[name] = len(self.sub_timers)
        t = Timer()
        self.sub_timers.append(t)
        return t
