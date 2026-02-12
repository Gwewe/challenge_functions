from lib.snippet_maker import snippet_maker

# A function called make_snippet that takes a string as an argument 
# - and returns the first five words 
# - and then a '...' if there are more than that.

'''
Given an empty string,
the function returns an empty string
'''
def test_given_empty_string_returns_empty_string():
    snippet = snippet_maker("")

    assert snippet == ""

'''
Given an four words string,
the function returns the same string as there are only 4 words
'''
def test_given_four_words_string_returns_the_same_string():
    text_source = "Today is Wednesday 11"
    snippet = snippet_maker(text_source)

    assert snippet == "Today is Wednesday 11"


'''
Given an five words string,
the function return the first five words
'''
def test_given_five_words_string_returns_first_five_words():
    text_source = "Today is Wednesday 11 February"
    snippet = snippet_maker(text_source)

    assert snippet == "Today is Wednesday 11 February"

'''
Given an six words string,
the function return the first five words and three dot
'''
def test_given_six_words_string_returns_first_five_words_and_three_dots():
    text_source = "Today is Wednesday 11 February 2025"
    snippet = snippet_maker(text_source)

    assert snippet == "Today is Wednesday 11 February..."

