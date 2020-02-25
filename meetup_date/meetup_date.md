# meetup_date

This week I'd like you to create a function that determines which day of the month the San Diego Python meetup should be. The San Diego Python meetup is on the fourth Thursday of the month (ignoring US holidays, during which we reschedule it).

Your function should accept year and month arguments and should return a datetime.date object representing the day of the month for the meetup.

    >>> meetup_date(2012, 3)
    datetime.date(2012, 3, 22)
    >>> meetup_date(2015, 2)
    datetime.date(2015, 2, 26)
    >>> meetup_date(2018, 6)
    datetime.date(2018, 6, 28)
    >>> meetup_date(2020, 1)
    datetime.date(2020, 1, 23)

You can do it with just the datetime module, but this problem can definitely be a bit tricky.

#### Bonus 1

For the first bonus, I'd like you to allow your `meetup_date` function to accept optional arguments that allow it to be used for other meetups as well.

The arguments, `nth` and `weekday`, will allow callers of your function to specify which weekday their meetup is held on and which occurrence in the month it is held (for example the 2nd Tuesday or the first Friday).

    >>> print("SD Python:", meetup_date(2015, 8, nth=4, weekday=3))
    SD Python: 2015-08-27
    >>> print("PyLadies on 4th Wed:", meetup_date(2018, 7, nth=4, weekday=2))
    PyLadies on 4th Wed: 2018-07-25
    >>> print("SDJS on 1st Tues:", meetup_date(2012, 2, nth=1, weekday=1))
    SDJS on 1st Tues: 2012-02-07

Note that the weekday argument accepts 0 to 6, mirroring the `date.weekday` method, not the `isoweekday` method (which is 1 to 7).

#### Bonus 2

For the second bonus, I'd like you to allow the nth argument to be a negative number, which means it should start counting from the end of the month.

    >>> print("SDHN on last Friday:", meetup_date(2010, 6, nth=-1, weekday=4))
    SDHN on last Friday: 2010-06-25
    >>> print("-1 != 4 (sometimes):", meetup_date(2020, 1, nth=-1, weekday=4))
    -1 != 4 (sometimes): 2020-01-31

This one is a bit tricky because there are often a couple weekdays with 5 occurrences in a given month.

#### Bonus 3

For the third bonus, I'd like you to create a `Weekday` object that can be used to more clearly specify days without using magic numbers:

    >>> print("SDJS", meetup_date(2012, 2, nth=1, weekday=Weekday.TUESDAY))
    SDJS 2012-02-07
    >>> print("PyLadies", meetup_date(2018, 7, nth=2, weekday=Weekday.WEDNESDAY))
    PyLadies 2018-07-11
    >>> print("SDHN", meetup_date(2010, 6, nth=-1, weekday=Weekday.FRIDAY))
    SDHN 2010-06-25
