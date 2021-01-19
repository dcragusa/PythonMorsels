import unittest

from chainsequence import ChainSequence


class ChainSequenceTests(unittest.TestCase):

    """Tests for ChainSequence."""

    def test_indexable(self):
        x = [1, 2, 3]
        y = (4, 5, 6)
        chain = ChainSequence(x, y)
        self.assertEqual(chain[0], 1)
        self.assertEqual(chain[3], 4)
        self.assertEqual(chain[-1], 6)
        self.assertEqual(chain[-4], 3)
        self.assertEqual(chain[1], 2)
        self.assertEqual(chain[4], 5)

    def test_indexing_large_sequences_lazily(self):
        x = range(1, 10000, 2)
        y = range(50000, 0, -1)
        z = range(10000000)
        chain = ChainSequence(x, y, z)
        self.assertEqual(chain[0], 1)
        self.assertEqual(chain[3], 7)
        self.assertEqual(chain[-1], 9999999)
        self.assertEqual(chain[-4], 9999996)
        self.assertEqual(chain[1], 3)
        self.assertEqual(chain[4], 9)

    def test_has_length(self):
        self.assertEqual(len(ChainSequence([1, 2, 3], (4, 5, 6))), 6)
        self.assertEqual(len(ChainSequence('hi', [0, 1, 2], (3, 4, 5))), 8)

    def test_can_be_looped_over_multiple_times(self):
        chain = ChainSequence([1, 2, 3], (4, 5, 6))
        self.assertEqual(list(chain), [1, 2, 3, 4, 5, 6])
        self.assertEqual(tuple(chain), (1, 2, 3, 4, 5, 6))

    def test_changing_wrapped_sequence_changes_chainsequence(self):
        numbers = [1, 2, 3]
        word = 'hello'
        chain = ChainSequence(numbers, word)
        self.assertEqual(len(chain), 8)
        self.assertEqual(chain[4], 'e')
        self.assertEqual(chain[3], 'h')
        numbers.append(9)
        self.assertEqual(len(chain), 9)
        self.assertEqual(chain[4], 'h')
        self.assertEqual(chain[3], 9)

    def test_empty_sequences(self):
        chain = ChainSequence('hi', [], range(5), (), '')
        self.assertEqual(len(chain), 7)
        self.assertEqual(chain[1], 'i')
        self.assertEqual(chain[2], 0)
        self.assertEqual(chain[-1], 4)

    def test_sequences_attribute(self):
        sequences = ['hello', range(5), [True, False]]
        chain = ChainSequence(*sequences)
        self.assertEqual(chain.sequences, sequences)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_sliceability(self):
        chain = ChainSequence('hi', [2, 1, 3, 4, 7])
        view = chain[:4]
        self.assertEqual(list(view), ['h', 'i', 2, 1])
        chain.sequences[1] = 'ya!'
        self.assertEqual(list(view), ['h', 'i', 'y', 'a'])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_string_representations(self):
        chain = ChainSequence('hi', [2, 1, 3, 4, 7])
        self.assertEqual(str(chain), "ChainSequence('hi', [2, 1, 3, 4, 7])")
        self.assertEqual(repr(chain), "ChainSequence('hi', [2, 1, 3, 4, 7])")
        self.assertEqual(str(ChainSequence()), "ChainSequence()")
        self.assertEqual(
            str(ChainSequence("I don't know\n")),
            r"""ChainSequence("I don't know\n")""",
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_addition(self):
        chain1 = ChainSequence([2, 1], [3])
        chain2 = chain1 + [4, 7]
        self.assertEqual(list(chain2), [2, 1, 3, 4, 7])
        self.assertEqual(list(chain1), [2, 1, 3])
        chain3 = chain1
        self.assertIs(chain1, chain3)
        chain1 += [0, 9]
        self.assertIs(chain1, chain3)
        self.assertEqual(list(chain1), [2, 1, 3, 0, 9])
        self.assertEqual(list(chain2), [2, 1, 3, 4, 7])
        self.assertEqual(list(chain3), [2, 1, 3, 0, 9])


if __name__ == "__main__":
    unittest.main(verbosity=2)
