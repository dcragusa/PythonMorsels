# EasyDict

This week I'd like you to create a class called EasyDict which creates objects that can use key lookups and attribute lookups interchangeably:

    >>> person = EasyDict({'name': "Trey Hunner", 'location': "San Diego"})
    >>> person.name
    'Trey Hunner'
    >>> person['location']
    'San Diego'

At first your object should only worry about accessing keys and attributes and accepting a single dictionary as its one optional argument.

For the first bonus, I'd like you to make sure key and attribute assignment to works:

#### Bonus 1

    >>> person = EasyDict({'name': "Trey Hunner", 'location': "San Diego"})
    >>> person.location = "Portland"
    >>> person['location']
    'Portland'
    >>> person['location'] = "San Diego"
    >>> person.location
    'San Diego'

#### Bonus 2

For the second bonus, I'd like you to also allow your EasyDict class to accept keyword arguments, I'd like you to make EasyDict objects comparable to each other via equality, and I'd like you to implement a get method that works sort of like the get method on dictionaries:

    >>> person = EasyDict(name="Trey Hunner", location="San Diego")
    >>> person.location
    'San Diego'
    >>> person == EasyDict(name="Trey", location="San Diego")
    False
    >>> person == EasyDict(name="Trey Hunner", location="San Diego")
    True
    >>> person.get('profession')
    >>> person.get('profession', 'unknown')
    'unknown'
    >>> person.get('name', 'unknown')
    'Trey Hunner'

#### Bonus 3

For the third bonus, I'd like you to allow your EasyDict class to accept a normalize keyword argument which, if true, will "normalize" the spaces in keys to underscores in attributes:

    >>> person = EasyDict(name="Trey Hunner", location="San Diego", normalize=True)
    >>> person['company name'] = "Truthful Technology LLC"
    >>> person.company_name
    'Truthful Technology LLC'
    >>> person['company name']
    'Truthful Technology LLC'
