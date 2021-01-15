import random
import unittest
from time import sleep

from timer import Timer


class TimerTests(unittest.TestCase):

    """Tests for Timer."""

    _baseline = None

    @staticmethod
    def get_baseline(count=5):
        times = 0
        for i in range(count):
            with Timer() as timer:
                sleep(0)
            times += timer.elapsed
        return times / count

    def assertTimeEqual(self, actual, expected):
        if self._baseline is None:
            self._baseline = self.get_baseline()
        self.assertAlmostEqual(actual, self._baseline+expected, delta=0.005)

    def test_short_time(self):
        with Timer() as timer:
            sleep(0.01)
        self.assertGreater(timer.elapsed, 0.01)
        self.assertLess(timer.elapsed, 1)

    def test_very_short_time(self):
        with Timer() as timer:
            pass
        self.assertTimeEqual(timer.elapsed, 0)

    def test_two_timers(self):
        with Timer() as timer1:
            sleep(0.005)
            with Timer() as timer2:
                sleep(0.005)
            sleep(0.005)
        self.assertLess(timer2.elapsed, timer1.elapsed)

    def test_reusing_same_timer(self):
        timer = Timer()
        with timer:
            sleep(0.0005)
        elapsed1 = timer.elapsed
        with timer:
            sleep(0.004)
        self.assertLess(elapsed1, timer.elapsed)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_runs_recorded(self):
        timer1 = Timer()
        timer2 = Timer()
        with timer1:
            with timer2:
                sleep(0.001)
            with timer2:
                sleep(0.002)
        with timer1:
            sleep(0.001)
        with timer1:
            pass
        self.assertEqual(len(timer1.runs), 3)
        self.assertTimeEqual(timer1.runs[0], 0.003)
        self.assertTimeEqual(timer1.runs[1], 0.001)
        self.assertTimeEqual(timer1.runs[2], 0.000)
        self.assertEqual(len(timer2.runs), 2)
        self.assertTimeEqual(timer2.runs[0], 0.001)
        self.assertTimeEqual(timer2.runs[1], 0.002)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_works_as_decorator(self):
        @Timer
        def wait_randomly(*args, **kwargs):
            wait_time = round(random.uniform(0.007, 0.009), 3)
            sleep(wait_time)
            return wait_time, args, kwargs
        time, args, kwargs = wait_randomly(1, a=3)
        self.assertEqual(args, (1,))
        self.assertEqual(kwargs, {'a': 3})
        self.assertTimeEqual(wait_randomly.elapsed, time)
        self.assertEqual(wait_randomly.runs, [wait_randomly.elapsed])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_stat_recorded(self):
        wait = Timer(sleep)
        wait(0.002)
        wait(0.003)
        wait(0.005)
        wait(0.008)
        wait(0.003)
        wait(0.009)
        self.assertTimeEqual(wait.mean, 0.005)
        self.assertTimeEqual(wait.median, 0.004)
        self.assertTimeEqual(wait.min, 0.002)
        self.assertTimeEqual(wait.max, 0.009)


if __name__ == "__main__":
    unittest.main(verbosity=2)
