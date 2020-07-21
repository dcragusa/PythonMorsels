# ProxyDict

This week I'd like you to create a `ProxyDict` class which offers an immutable dictionary-like interface that wraps around a given dictionary.

    >>> user_data = {'name': 'Trey Hunner', 'active': False}
    >>> proxy_data = ProxyDict(user_data)
    >>> proxy_data.keys()
    dict_keys(['name', 'active'])
    >>> proxy_data['name']
    'Trey Hunner'
    >>> proxy_data['active']
    False
    >>> user_data['active'] = True
    >>> proxy_data['active']
    True
    >>> proxy_data['active'] = False
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'ProxyDict' object does not support item assignment

The `ProxyDict` class should support key lookups, the `keys` method, and equality with other dictionaries and other `ProxyDict` instances:

    >>> user_data = {'name': 'Trey Hunner', 'active': False}
    >>> p1 = ProxyDict(user_data)
    >>> p2 = ProxyDict(user_data.copy())
    >>> p1 == p2
    True
    >>> p2 == user_data
    True

#### Bonus 1

For the first bonus, I'd like you to make your `ProxyDict` class iterable, add support for the built-in `len`, and add appropriate `items`, `values`, and `get` methods.

    >>> user_data = {'name': 'Trey Hunner', 'active': False}
    >>> proxy_data = ProxyDict(user_data)
    >>> len(proxy_data)
    2
    >>> for key in proxy_data:
    ...     print(key)
    ...
    'name'
    'active'
    >>> proxy_data.items()
    dict_items([('name', 'Trey Hunner'), ('active', False)])
    >>> proxy_data.values()
    dict_values(['Trey Hunner', False])
    >>> proxy_data.get('name')
    'Trey Hunner'
    >>> proxy_data.get('shoe_size', 0)
    0

#### Bonus 2

For the second bonus, I'd like you to allow your `ProxyDict` class to accept any number of mapping arguments, not just one. In the case of mappings with the same key, the last one "wins" (its value is used).

    >>> user_data = {'name': 'Trey Hunner', 'active': False}
    >>> site_data = {'name': 'Python Morsels', 'last_updated': 1995}
    >>> proxy_data = ProxyDict(user_data, site_data)
    >>> proxy_data['name']
    'Python Morsels'
    >>> proxy_data['active']
    False
    >>> proxy_data['last_updated']
    1995
    >>> del site_data['name']
    >>> proxy_data['name']
    'Trey Hunner'

#### Bonus 3

For the third bonus, I'd like you to:
- make a `maps` attribute on your `ProxyDict` class which will contain a list of the mappings that are being proxied to.
- make a nice string representation for your class, showing each mapping in order


    >>> p = ProxyDict({0: 9, 1: 6}, {2: 8}, {3: 7})
    >>> p
    ProxyDict({0: 9, 1: 6}, {2: 8}, {3: 7})
    >>> p.maps
    [{0: 9, 1: 6}, {2: 8}, {3: 7}]
