import unittest
from time import sleep

from timer_revisited import Timer


class TimerTests(unittest.TestCase):

    """Tests for Timer."""

    def test_short_time(self):
        with Timer() as timer:
            sleep(0.01)
        self.assertAlmostEqual(timer.elapsed, 0.01, places=2)

    def test_very_short_time(self):
        with Timer() as timer:
            pass
        self.assertAlmostEqual(timer.elapsed, 0.000, places=3)

    def test_two_timers(self):
        with Timer() as timer1:
            sleep(0.01)
            with Timer() as timer2:
                sleep(0.01)
            sleep(0.01)
        self.assertAlmostEqual(timer1.elapsed, 0.03, places=2)
        self.assertAlmostEqual(timer2.elapsed, 0.01, places=2)

    def test_reusin_same_timer(self):
        timer = Timer()
        with timer:
            sleep(0.01)
        self.assertAlmostEqual(timer.elapsed, 0.01, places=2)
        with timer:
            sleep(0.02)
        self.assertAlmostEqual(timer.elapsed, 0.02, places=2)

    def test_runs_recorded(self):
        timer1 = Timer()
        timer2 = Timer()
        with timer1:
            with timer2:
                sleep(0.01)
            with timer2:
                sleep(0.02)
        with timer1:
            sleep(0.01)
        with timer1:
            pass
        self.assertEqual(len(timer1.runs), 3)
        self.assertAlmostEqual(timer1.runs[0], 0.03, places=2)
        self.assertAlmostEqual(timer1.runs[1], 0.01, places=2)
        self.assertAlmostEqual(timer1.runs[2], 0.00, places=2)
        self.assertEqual(len(timer2.runs), 2)
        self.assertAlmostEqual(timer2.runs[0], 0.01, places=2)
        self.assertAlmostEqual(timer2.runs[1], 0.02, places=2)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_split(self):
        with Timer() as timer1:
            with timer1.split() as timer2:
                sleep(0.01)
            with timer1.split() as timer3:
                sleep(0.02)
            with timer1.split() as timer4:
                sleep(0.03)
        self.assertAlmostEqual(timer1.elapsed, 0.06, places=2)
        self.assertAlmostEqual(timer2.elapsed, 0.01, places=2)
        self.assertAlmostEqual(timer3.elapsed, 0.02, places=2)
        self.assertAlmostEqual(timer4.elapsed, 0.03, places=2)
        self.assertEqual(timer1[0].elapsed, timer2.elapsed)
        self.assertEqual(timer1[1].elapsed, timer3.elapsed)
        self.assertEqual(timer1[2].elapsed, timer4.elapsed)
        self.assertEqual(len(timer1.runs), 1)
        self.assertEqual(len(timer2.runs), 1)
        self.assertEqual(len(timer3.runs), 1)
        self.assertEqual(len(timer4.runs), 1)
        with self.assertRaises(Exception):
            with timer1.split():
                print("timer split when it wasn't running!")

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_named_split(self):
        sleeps = [0.02, 0.01, 0.04, 0.03]
        with Timer() as timer:
            for n in sleeps:
                with timer.split('sleep'):
                    sleep(n)
        self.assertEqual(len(timer['sleep'].runs), 4)
        runs = timer['sleep'].runs
        self.assertAlmostEqual(runs[0], 0.02, places=2)
        self.assertAlmostEqual(runs[1], 0.01, places=2)
        self.assertAlmostEqual(runs[2], 0.04, places=2)
        self.assertAlmostEqual(runs[3], 0.03, places=2)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_globally_named_timer(self):
        timer1 = Timer('t1')
        timer2 = Timer('t1')
        timer3 = Timer('t2')
        with timer1:
            sleep(0.01)
        self.assertEqual(len(timer1.runs), 1)
        self.assertEqual(len(timer2.runs), 1)
        self.assertEqual(len(timer3.runs), 0)
        with timer2:
            pass
        self.assertEqual(len(timer1.runs), 2)
        self.assertEqual(len(timer2.runs), 2)
        self.assertEqual(len(timer3.runs), 0)
        with timer3:
            sleep(0.01)
        self.assertEqual(len(timer1.runs), 2)
        self.assertEqual(len(timer3.runs), 1)
        self.assertAlmostEqual(timer1.runs[0], 0.01, places=2)
        self.assertAlmostEqual(timer1.runs[1], 0.00, places=2)
        self.assertEqual(timer1.runs, timer2.runs)
        self.assertEqual(timer1.elapsed, timer2.elapsed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
