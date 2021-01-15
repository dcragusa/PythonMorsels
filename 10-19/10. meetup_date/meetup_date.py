import datetime

# def 10. meetup_date(year, month):
#     first_day_weekday = datetime.date(year, month, 1).weekday()
#     num_weeks = 3 if first_day_weekday <= 3 else 4
#     return datetime.date(year, month, 1 + (num_weeks*7) + (3-first_day_weekday))

# def 10. meetup_date(year, month, nth=4, weekday=3):
#     first_day_weekday = datetime.date(year, month, 1).weekday()
#     num_weeks = nth-1 if first_day_weekday <= weekday else nth
#     return datetime.date(year, month, 1 + (num_weeks*7) + (weekday-first_day_weekday))


class Weekday:
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(0, 7)


def meetup_date(year, month, nth=4, weekday=3):
    first_day_weekday = datetime.date(year, month, 1).weekday()
    if nth < 0:
        try:
            # if this doesn't ValueError there are 5 occurrences of the day
            datetime.date(year, month, 1 + 28 + (weekday-first_day_weekday))
            num_weeks = 5 + nth
        except ValueError:
            num_weeks = 4 + nth
    else:
        num_weeks = nth-1 if first_day_weekday <= weekday else nth
    return datetime.date(year, month, 1 + (num_weeks*7) + (weekday-first_day_weekday))
