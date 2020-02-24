# OrderedSet

This week I'd like you to make an OrderedSet class. This class should work like a set, but it should also maintain the insertion order of the items added to it (unlike Python's built-in set which is unordered).

    ordered_words = ['these', 'are', 'words', 'in', 'an', 'order']
    >>> print(*set(ordered_words))
    order these are in an words
    >>> print(*OrderedSet(ordered_words))
    these are words in an order
    >>> print(*OrderedSet(['repeated', 'words', 'are', 'not', 'repeated']))
    repeated words are not

This set should be relatively memory efficient and containment checks should be relatively time efficient:

    >>> words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
    >>> len(words)
    4
    >>> 'hello' in words
    True

Initially you don't have to worry about allowing sets to be modified after they've been made. Just focus on getting len and the in operator.

#### Bonus 1

For the first bonus, I'd like you to make sure your set works with the add and discard methods:

    >>> words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
    >>> words.add('doing')
    >>> print(*words)
    hello how are you doing
    >>> words.discard('Python!')
    >>> words.discard('are')
    >>> print(*words)
    hello how you doing

The add and discard method should work just like those on sets (you can add or discard the same thing twice).

#### Bonus 2

For the second bonus, I'd like you to make your OrderedSet class support equality. If an OrderedSet is compared to another OrderedSet, they'll only be seen as equal if the order is the same. If an OrderedSet is compared to an unordered set, the order is ignored during the comparison. If an OrderedSet is compared to a non-set, the comparison should evaluate as False (unless the other object implements equality with ordered sets.

    >>> OrderedSet(['how', 'are', 'you']) == OrderedSet(['how', 'you', 'are'])
    False
    >>> OrderedSet(['how', 'are', 'you']) == {'how', 'you', 'are'}
    True
    >>> OrderedSet(['how', 'are', 'you']) == ['how', 'are', 'you']
    False

#### Bonus 3

For the third bonus, I'd like your OrderedSet class to support indexing:

    >>> words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
    >>> words[1]
    'how'
    >>> words[-1]
    'you'
