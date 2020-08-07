# reconcile_accounts

This week I'd like you to write a function that helps reconcile two groups of financial transactions.

Your function, `reconcile_accounts`, should accept two lists-of-lists (representing rows of financial data) and should 
return copies of those two list-of-lists with another column added to the end that notes whether the transaction was 
`FOUND` in the other lists or was `MISSING` from them.

The lists of lists will include data specified in four columns:

    Date (in YYYY-MM-DD format)
    Department
    Amount
    Payee

All of the columns will be represented as strings.

Given the file `transactions1.csv`:

    2000-12-04,Engineering,16.00,Python Morsels
    2000-12-04,Finance,60.00,Quick Books
    2000-12-05,Engineering,50.00,Zapier

And the file `transactions2.csv`:

    2000-12-04,Engineering,16.00,Python Morsels
    2000-12-05,Engineering,49.99,Zapier
    2000-12-04,Finance,60.00,Quick Books

Your reconcile_accounts function should work like this:

    >>> import csv
    >>> from pathlib import Path
    >>> from pprint import pprint
    >>> transactions1 = list(csv.reader(Path('transactions1.csv').open()))
    >>> transactions2 = list(csv.reader(Path('transactions2.csv').open()))
    >>> out1, out2 = reconcile_accounts(transactions1, transactions2)
    >>> pprint(out1)
    [['2000-12-04', 'Engineering', '16.00', 'Python Morsels', 'FOUND'],
     ['2000-12-04', 'Finance', '60.00', 'Quick Books', 'FOUND'],
     ['2000-12-05', 'Engineering', '50.00', 'Zapier', 'MISSING']]
    >>> pprint(out2)
    [['2000-12-04', 'Engineering', '16.00', 'Python Morsels', 'FOUND'],
     ['2000-12-05', 'Engineering', '49.99', 'Zapier', 'MISSING'],
     ['2000-12-04', 'Finance', '60.00', 'Quick Books', 'FOUND']]

For transactions to be considered the same, their date, department, amount, and payee should match exactly.

The order of the transactions in each file shouldn't matter.

#### Bonus 1

For the first bonus, make sure that each file works properly when there are duplicate transactions (each transaction 
can only correspond to one other transaction).

#### Bonus 2

For the second bonus, each transaction should be able to match with a corresponding that transaction that has a date 
up to one day in the future or the past but is otherwise the same. For otherwise duplicate transactions with different 
dates, the transaction in the first list should pair with the earliest (by date) matching transaction in the second 
list. For example, a transaction in the first list with the date `2018-12-25` should match with a still-unmatched 
`2018-12-24` dated transaction in the second list before an otherwise equivalent `2018-12-25` or `2018-12-26`-dated 
transaction.
