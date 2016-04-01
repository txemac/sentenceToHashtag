import unittest
from sentenceToHashtag import sentence_to_hashtag


__author__ = 'josebermudez'


class TestSentenceToHastag(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSentenceToHastag, self).__init__(*args, **kwargs)

    def test_example(self):
        sentence = 'thi9s Is &&So cool'
        expected_out = '#ThisIsSoCool'
        out = sentence_to_hashtag(sentence)
        self.assertEqual(out, expected_out)

    def test_none(self):
        sentence = None
        out = sentence_to_hashtag(sentence)
        self.assertIsNone(out)

    def test_integer(self):
        sentence = 123
        out = sentence_to_hashtag(sentence)
        self.assertIsNone(out)

    def test_wihout_letters(self):
        sentence = '123'
        out = sentence_to_hashtag(sentence)
        self.assertIsNone(out)
