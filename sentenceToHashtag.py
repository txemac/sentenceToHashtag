from string import ascii_letters


__author__ = "josebermudez"


def sentence_to_hashtag(sentence):
    """
    This function convert a sentence in a hashtag.
    Non-alphabetic characters are ignored.
    E.g. 'thi9s Is &&So cool' -> '#ThisIsSoCool'.
    :param sentence: sentence
    :return: hashtag
    """
    result = None

    if sentence and type(sentence) is str:
        result = '#'

        for word in sentence.split():
            # clean non-alphabetic characters
            aux = "".join([ch for ch in word if ch in ascii_letters])

            # add capitalize word
            result += aux.title()

    if result == '#':
        result = None

    return result
