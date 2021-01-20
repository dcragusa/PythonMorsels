import unittest

from sequencezip_revisited import SequenceZip


class SequenceZipTests(unittest.TestCase):

    """Tests for SequenceZip."""

    def test_constructor(self):
        SequenceZip([1, 2, 3, 4])
        SequenceZip(range(5), [1, 2, 3, 4])
        SequenceZip(range(5), [1, 2, 3, 4], 'hello there')
        SequenceZip([1], [3], [4, 5], [7], [8, 9])

    def test_length(self):
        self.assertEqual(len(SequenceZip([1, 2, 3, 4])), 4)
        self.assertEqual(len(SequenceZip(range(5), [1, 2, 3, 4])), 4)
        self.assertEqual(len(SequenceZip(range(5), [1, 2, 4], 'hello there')), 3)

    def test_indexing(self):
        seq = SequenceZip(range(5), [1, 2, 4], 'hello there')
        self.assertEqual(seq[0], (0, 1, 'h'))
        self.assertEqual(seq[2], (2, 4, 'l'))
        self.assertEqual(seq[-1], seq[2])
        with self.assertRaises(IndexError):
            seq[3]

    def test_sequence_not_copied(self):
        x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
        seq1 = SequenceZip(x, y, z)
        self.assertEqual(seq1[-1], (3, 6, 9))
        x[-1], z[-1] = z[-1], x[-1]
        self.assertEqual(seq1[-1], (9, 6, 3))
        many_large_sequences = [range(1000000) for _ in range(100)]
        seq2 = SequenceZip(*many_large_sequences)
        self.assertEqual(seq2[-1], (999999,) * 100)

    def test_iterable(self):
        seq = SequenceZip(range(5), [1, 2, 4], 'hello there')
        self.assertEqual(list(seq), [
            (0, 1, 'h'),
            (1, 2, 'e'),
            (2, 4, 'l'),
        ])

    def test_equality(self):
        seq1 = SequenceZip([1, 2, 3], [4, 5, 6], [7, 8, 9])
        seq2 = SequenceZip([1, 2, 3], [4, 5, 6], [7, 8, 9, 0])
        seq3 = SequenceZip([1, 2, 3], [4, 5, 4], [7, 8, 9, 0])
        self.assertEqual(seq1, seq2)
        self.assertNotEqual(seq1, seq3)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_slicing(self):
        seq = SequenceZip(range(5), [1, 2, 3, 4], 'hiya!')
        self.assertEqual(list(seq[0:2]), [
            (0, 1, 'h'),
            (1, 2, 'i'),
        ])
        self.assertEqual(list(seq[1:-1]), [
            (1, 2, 'i'),
            (2, 3, 'y'),
        ])
        self.assertEqual(list(seq[:-1]), [
            (0, 1, 'h'),
            (1, 2, 'i'),
            (2, 3, 'y'),
        ])
        self.assertEqual(list(seq[-3:]), [
            (1, 2, 'i'),
            (2, 3, 'y'),
            (3, 4, 'a'),
        ])
        self.assertEqual(list(seq[:2]), [
            (0, 1, 'h'),
            (1, 2, 'i'),
        ])
        self.assertEqual(list(seq[::-1]), [
            (3, 4, 'a'),
            (2, 3, 'y'),
            (1, 2, 'i'),
            (0, 1, 'h'),
        ])
        self.assertEqual(list(seq[::-2]), [
            (3, 4, 'a'),
            (1, 2, 'i'),
        ])
        self.assertEqual(type(seq[-2:]), SequenceZip)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_assigning_and_deleting(self):
        x, y, z = [0, 1, 2, 3], [4, 5, 6], [7, 8, 9, 10]
        seq = SequenceZip(x, y, z)
        seq[0] = (-1, -2, -3)
        self.assertEqual(seq[0], (-1, -2, -3))
        seq[-1] = (-4, -5, -6)
        self.assertEqual(x, [-1, 1, -4, 3])
        self.assertEqual(y, [-2, 5, -5])
        self.assertEqual(z, [-3, 8, -6, 10])
        del seq[-2]
        self.assertEqual(x, [-1, -4, 3])
        self.assertEqual(y, [-2, -5])
        self.assertEqual(z, [-3, -6, 10])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_appending_and_inserting(self):
        x, y, z = [0, 1, 2, 3], [4, 5, 6], [7, 8, 9, 10]
        seq = SequenceZip(x, y, z)
        seq.insert(0, (9, 5, 0))
        self.assertEqual(seq[0], (9, 5, 0))
        self.assertEqual(x, [9, 0, 1, 2, 3])
        self.assertEqual(y, [5, 4, 5, 6])
        self.assertEqual(z, [0, 7, 8, 9, 10])
        seq.append((-9, -8, -7))
        self.assertEqual(seq[-1], (-9, -8, -7))
        self.assertEqual(x, [9, 0, 1, 2, -9])
        self.assertEqual(y, [5, 4, 5, 6, -8])
        self.assertEqual(z, [0, 7, 8, 9, -7])
        with self.assertRaises(Exception):
            seq.append((1, 2))
        with self.assertRaises(Exception):
            seq.append((3, 4, 5, 6))


if __name__ == "__main__":
    unittest.main(verbosity=2)
