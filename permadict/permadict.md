# PermaDict

This week you're going to create a dictionary-like class that disallows keys to be updated (they can only be added or removed).

The `PermaDict` class should allow keys to be added and deleted, just like any other dictionary:

    >>> locations = PermaDict({'Trey': "San Diego", 'Al': "San Francisco"})
    >>> locations['Harry'] = "London"
    >>> locations.update({'Russell': "Perth", 'Katie': "Sydney"})
    >>> locations['Trey']
    'San Diego'

And your `PermaDict` class should have keys, values, and items methods and should be iterable just like a dictionary:

    >>> locations = PermaDict([('Kojo', "Houston"), ('Tracy', "Toronto")])
    >>> list(locations)
    ['Kojo', 'Tracy']
    >>> list(locations.keys())
    ['Kojo', 'Tracy']
    >>> list(locations.values())
    ['Houston', 'Toronto']
    >>> for name, place in locations.items():
    ...     print(f"{name} in {place}")
    ...
    Kojo in Houston
    Tracy in Toronto

But unlike a dictionary when a value is set and for a key that already exists, a `KeyError` exception should be raised:

    >>> locations = PermaDict({'David': "Boston"})
    >>> locations['David'] = "Amsterdam"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 5, in __setitem__
    KeyError: "'David' already in dictionary."
    >>> locations['Asheesh'] = "Boston"
    >>> locations.update({'Asheesh': "San Francisco"})
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 5, in update
    KeyError: "'Asheesh' already in dictionary."
    >>> locations
    {'David': 'Boston', 'Asheesh': 'Boston'}

#### Bonus 1

For the first bonus, I'd like you to add a force_set method to your `PermaDict` class which allows keys to be updated without error.

    >>> locations = PermaDict({'David': "Boston"})
    >>> locations.force_set('David', "Amsterdam")
    >>> locations.force_set('Asheesh', "Boston")
    >>> locations.force_set('Asheesh', "San Francisco")
    >>> locations
    {'David': 'Amsterdam', 'Asheesh': 'San Francisco'}

#### Bonus 2

For the second bonus, I'd like you to handle an optional `silent` keyword argument passed to the initializer of your dictionary to allow your dictionary to silently ignore updates to existing keys.

    >>> locations = PermaDict({'David': "Boston"}, silent=True)
    >>> locations['David'] = "Amsterdam"
    >>> locations['Asheesh'] = "Boston"
    {'David': 'Boston', 'Asheesh': 'Boston'}

#### Bonus 3

For the third bonus, I'd like your `PermaDict` class's `update` method to handle an optional `force` keyword argument to allow your dictionary's `update` method to force update the values for existing keys.

    >>> locations = PermaDict({'David': "Boston"})
    >>> locations.update([('David', 'Amsterdam'), ('Asheesh', 'SF')], force=True)
    >>> locations
    {'David': 'Amsterdam', 'Asheesh': 'SF'}
