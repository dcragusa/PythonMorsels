import unittest

from reconcile_accounts import reconcile_accounts


class ReconcileAccountsTests(unittest.TestCase):

    """Tests for reconcile_accounts."""

    maxDiff = None

    def test_no_transactions(self):
        self.assertEqual(
            reconcile_accounts([], []),
            ([], [])
        )

    def test_one_transaction_each(self):
        records1 = [
            ['2017-05-01', 'Fishing', '50.80', 'Fish Market'],
        ]
        records2 = [
            ['2017-05-01', 'Fishing', '50.80', 'Fish Market'],
        ]
        results1 = [
            ['2017-05-01', 'Fishing', '50.80', 'Fish Market', 'FOUND'],
        ]
        results2 = [
            ['2017-05-01', 'Fishing', '50.80', 'Fish Market', 'FOUND'],
        ]
        self.assertEqual(
            reconcile_accounts(records1, records2),
            (results1, results2)
        )

    def test_one_missing_transaction(self):
        records1 = [
            ['2017-05-01', 'Fishing', '50.80', 'Fish Market'],
            ['2017-05-01', 'Fishing', '-10.00', 'Bait Store'],
            ['2017-05-02', 'Fishing', '6.00', 'Donut Shop'],
            ['2017-05-02', 'Fishing', '12.00', 'Pizza Place'],
        ]
        records2 = [
            ['2017-05-01', 'Fishing', '50.80', 'Fish Market'],
            ['2017-05-01', 'Fishing', '-10.00', 'Bait Store'],
            ['2017-05-02', 'Fishing', '12.00', 'Pizza Place'],
        ]
        results1 = [
            ['2017-05-01', 'Fishing', '50.80', 'Fish Market', 'FOUND'],
            ['2017-05-01', 'Fishing', '-10.00', 'Bait Store', 'FOUND'],
            ['2017-05-02', 'Fishing', '6.00', 'Donut Shop', 'MISSING'],
            ['2017-05-02', 'Fishing', '12.00', 'Pizza Place', 'FOUND'],
        ]
        results2 = [
            ['2017-05-01', 'Fishing', '50.80', 'Fish Market', 'FOUND'],
            ['2017-05-01', 'Fishing', '-10.00', 'Bait Store', 'FOUND'],
            ['2017-05-02', 'Fishing', '12.00', 'Pizza Place', 'FOUND'],
        ]
        self.assertEqual(
            reconcile_accounts(records1, records2),
            (results1, results2)
        )
        self.assertEqual(
            reconcile_accounts(records2, records1),
            (results2, results1)
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_duplicate_transactions(self):
        records1 = [
            ['2017-05-01', 'A', '50.80', 'a'],
            ['2017-05-01', 'B', '-10.00', 'a'],
            ['2017-05-01', 'A', '50.80', 'a'],
        ]
        records2 = [
            ['2017-05-01', 'A', '50.80', 'a'],
            ['2017-05-01', 'B', '-10.00', 'a'],
            ['2017-05-01', 'A', '50.80', 'a'],
            ['2017-05-01', 'A', '50.80', 'a'],
        ]
        results1 = [
            ['2017-05-01', 'A', '50.80', 'a', 'FOUND'],
            ['2017-05-01', 'B', '-10.00', 'a', 'FOUND'],
            ['2017-05-01', 'A', '50.80', 'a', 'FOUND'],
        ]
        results2 = [
            ['2017-05-01', 'A', '50.80', 'a', 'FOUND'],
            ['2017-05-01', 'B', '-10.00', 'a', 'FOUND'],
            ['2017-05-01', 'A', '50.80', 'a', 'FOUND'],
            ['2017-05-01', 'A', '50.80', 'a', 'MISSING'],
        ]
        self.assertEqual(
            reconcile_accounts(records1, records2),
            (results1, results2)
        )
        self.assertEqual(
            reconcile_accounts(records2, records1),
            (results2, results1)
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_transactions_match_nearby_days(self):
        records1 = [
            ['2017-05-02', 'A', '1.00', 'a'],
            ['2017-05-12', 'A', '5.00', 'a'],
            ['2017-04-30', 'A', '1.00', 'a'],
            ['2017-05-01', 'A', '1.00', 'a'],
        ]
        records2 = [
            ['2017-05-13', 'A', '5.00', 'a'],
            ['2017-05-02', 'A', '1.00', 'a'],
            ['2017-05-01', 'A', '1.00', 'a'],
        ]
        results1 = [
            ['2017-05-02', 'A', '1.00', 'a', 'MISSING'],
            ['2017-05-12', 'A', '5.00', 'a', 'FOUND'],
            ['2017-04-30', 'A', '1.00', 'a', 'FOUND'],
            ['2017-05-01', 'A', '1.00', 'a', 'FOUND'],
        ]
        results2 = [
            ['2017-05-13', 'A', '5.00', 'a', 'FOUND'],
            ['2017-05-02', 'A', '1.00', 'a', 'FOUND'],
            ['2017-05-01', 'A', '1.00', 'a', 'FOUND'],
        ]
        self.assertEqual(
            reconcile_accounts(records1, records2),
            (results1, results2)
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
