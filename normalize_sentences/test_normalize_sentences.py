from textwrap import dedent
import unittest


from normalize_sentences import normalize_sentences


class NormalizeSentencesTests(unittest.TestCase):

    """Tests for normalize_sentences."""

    maxDiff = 1000

    def test_no_sentences(self):
        sentence = "This isn't a sentence"
        self.assertEqual(normalize_sentences(sentence), sentence)

    def test_one_sentence(self):
        sentence = "This is a sentence."
        self.assertEqual(normalize_sentences(sentence), sentence)

    def test_two_sentences(self):
        sentences = ["Sentence 1.", "Sentence 2."]
        self.assertEqual(
            normalize_sentences(" ".join(sentences)),
            "  ".join(sentences),
        )

    def test_multiple_punctuation_marks(self):
        sentences = ["Sentence 1!", "Sentence 2?", "Sentence 3."]
        self.assertEqual(
            normalize_sentences(" ".join(sentences)),
            "  ".join(sentences),
        )

    def test_multiple_paragraphs(self):
        sentences = dedent("""
            This is a paragraph. With two sentences in it.

            And this is one. With three. Three short sentences.
        """).strip()
        expected = dedent("""
            This is a paragraph.  With two sentences in it.

            And this is one.  With three.  Three short sentences.
        """).strip()
        self.assertEqual(
            normalize_sentences(sentences),
            expected,
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_no_extra_spaces(self):
        sentences = """
            Sentence 1.  And two spaces after. But one space after this.
        """
        expected = """
            Sentence 1.  And two spaces after.  But one space after this.
        """
        self.assertEqual(
            normalize_sentences(sentences),
            expected,
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_with_abbreviations_and_numbers(self):
        sentences = "P.S. I like fish (e.g. salmon). That is all."
        expected = "P.S. I like fish (e.g. salmon).  That is all."
        self.assertEqual(
            normalize_sentences(sentences),
            expected,
        )
        sentences = "I ate 5.5 oranges. They cost $.50 each. They were good."
        expected = "I ate 5.5 oranges.  They cost $.50 each.  They were good."
        self.assertEqual(
            normalize_sentences(sentences),
            expected,
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_excluded_words_work(self):
        sentences = (
            "Do you know about the work of Dr. Rosalind Franklin? You can "
            "find out what she did by using google.com. Google is used by "
            "1.17 billion people (as of December 2012). That's a lot people!"
        )
        expected = (
            "Do you know about the work of Dr. Rosalind Franklin?  You can "
            "find out what she did by using google.com.  Google is used by "
            "1.17 billion people (as of December 2012).  That's a lot people!"
        )
        self.assertEqual(
            normalize_sentences(sentences),
            expected,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
