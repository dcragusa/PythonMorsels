import datetime
import unittest

from meetup_date import meetup_date


class MeetupDateTests(unittest.TestCase):

    """Tests for meetup_date."""

    def test_aug_2015(self):
        self.assertEqual(meetup_date(2015, 8), datetime.date(2015, 8, 27))

    def test_sept_2015(self):
        self.assertEqual(meetup_date(2015, 9), datetime.date(2015, 9, 24))

    def test_oct_2015(self):
        self.assertEqual(meetup_date(2015, 10), datetime.date(2015, 10, 22))

    def test_jan_2016(self):
        self.assertEqual(meetup_date(2016, 1), datetime.date(2016, 1, 28))

    def test_feb_2016(self):
        self.assertEqual(meetup_date(2016, 2), datetime.date(2016, 2, 25))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_allow_week_and_weekday_to_be_specified(self):
        # Fourth Thursday
        self.assertEqual(
            meetup_date(2016, 2, nth=4, weekday=3),
            datetime.date(2016, 2, 25),
        )
        # First Monday
        self.assertEqual(
            meetup_date(2018, 1, nth=1, weekday=0),
            datetime.date(2018, 1, 1),
        )
        # Fourth Saturday
        self.assertEqual(
            meetup_date(2018, 1, nth=4, weekday=5),
            datetime.date(2018, 1, 27),
        )
        # Fifth Wednesday
        self.assertEqual(
            meetup_date(2018, 1, nth=5, weekday=2),
            datetime.date(2018, 1, 31),
        )
        # Second Tuesday
        self.assertEqual(
            meetup_date(2018, 2, nth=2, weekday=1),
            datetime.date(2018, 2, 13),
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_allow_specifying_from_end_of_month(self):
        # Last Thursday
        self.assertEqual(
            meetup_date(2016, 2, nth=-1, weekday=3),
            datetime.date(2016, 2, 25),
        )
        # Last Friday
        self.assertEqual(
            meetup_date(2018, 1, nth=-1, weekday=4),
            datetime.date(2018, 1, 26),
        )
        # Last Wednesday
        self.assertEqual(
            meetup_date(2018, 1, nth=-1, weekday=2),
            datetime.date(2018, 1, 31),
        )
        # Last Saturday
        self.assertEqual(
            meetup_date(2018, 3, nth=-1, weekday=5),
            datetime.date(2018, 3, 31),
        )
        # Second to last Monday
        self.assertEqual(
            meetup_date(2018, 1, nth=-2, weekday=0),
            datetime.date(2018, 1, 22),
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_add_Weekday_object(self):
        from meetup_date import Weekday
        # First Monday
        self.assertEqual(
            meetup_date(2018, 1, nth=1, weekday=Weekday.MONDAY),
            datetime.date(2018, 1, 1),
        )
        # Second Tuesday
        self.assertEqual(
            meetup_date(2018, 2, nth=2, weekday=Weekday.TUESDAY),
            datetime.date(2018, 2, 13),
        )
        # Fifth Wednesday
        self.assertEqual(
            meetup_date(2018, 1, nth=5, weekday=Weekday.WEDNESDAY),
            datetime.date(2018, 1, 31),
        )
        # Fourth Thursday
        self.assertEqual(
            meetup_date(2016, 2, nth=4, weekday=Weekday.THURSDAY),
            datetime.date(2016, 2, 25),
        )
        # Last Friday
        self.assertEqual(
            meetup_date(2018, 1, nth=-1, weekday=Weekday.FRIDAY),
            datetime.date(2018, 1, 26),
        )
        # Last Saturday
        self.assertEqual(
            meetup_date(2018, 6, nth=-1, weekday=Weekday.SATURDAY),
            datetime.date(2018, 6, 30),
        )
        # Fourth Sunday
        self.assertEqual(
            meetup_date(2018, 6, nth=4, weekday=Weekday.SUNDAY),
            datetime.date(2018, 6, 24),
        )
        self.assertEqual(Weekday.MONDAY, 0)
        self.assertEqual(Weekday.TUESDAY, 1)
        self.assertEqual(Weekday.WEDNESDAY, 2)
        self.assertEqual(Weekday.THURSDAY, 3)
        self.assertEqual(Weekday.FRIDAY, 4)
        self.assertEqual(Weekday.SATURDAY, 5)
        self.assertEqual(Weekday.SUNDAY, 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
