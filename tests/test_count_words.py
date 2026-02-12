from lib.count_words import count_words

# A function called count_words that takes a string as an argument 
# - and returns the number of words in that string.

'''
Given an empty string with a space,
the function returns 0 for the count of words
'''
def test_given_empty_string_returns_zero_for_count():
    count = count_words(" ")

    assert count == 0


'''
Given a string with one word,
the function returns 1 for the count of words
'''
def test_given_one_word_string_returns_one_for_count():
    count = count_words("hello")

    assert count == 1


'''
Given a string with two words,
the function returns w for the count of words
'''
def test_given_two_word_string_returns_two_for_count():
    count = count_words("hello Wewe")

    assert count == 2


'''
Given a string with one word with leading and trailling space,
the function returns w for the count of words
'''
def test_given_one_word_with_whitespace_returns_one_for_count():
    count = count_words(" Wewe ")

    assert count == 1