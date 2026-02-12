from lib.text_checker import text_checker

"""
Given a sentence starting with an uppercase word and ending with a dot
It returns True
"""
def test_given_valid_sentence_returns_true():
    grammar_check = text_checker("Hello, Bruce Wayne.") 
    
    assert grammar_check == True


"""
Given a sentence not starting or ending with the proper conditions.
It returns False
"""
def test_given_a_sentence_with_no_valid_staring_nor_ending_characters():
    grammar_check = text_checker("oh, your name is luffy") 
    
    assert grammar_check == False


"""
Given a sentence starting with an uppercase and ending with a question mark,
It returns True
"""
def test_given_sentence_with_valid_start_and_question_mark_ending():
    grammar_checker = text_checker("Are you a superhero?") 
    
    assert grammar_checker == True



"""
Given a sentence starting with an uppercase and ending with a exclamation mark,
It returns True
"""
def test_given_sentence_with_valid_start_and_exclamation_mark_ending():
    grammar_checker = text_checker("You are a superhero!") 
    assert grammar_checker == True


"""
Given a sentence starting with capital letter but ending with comma.
It returns False
"""
def test_given_sentence_with_valid_start_and_comma_ending():
    grammar_checker = text_checker("Oh, my god, you are a pirate,") 
    assert grammar_checker == False

"""
Given a sentence starting with capital letter but ending with colons.
It returns False
"""
def test_given_sentence_with_valid_start_and_colons_ending():
    grammar_checker = text_checker("Oh, my god, you are a pirate:") 
    assert grammar_checker == False


"""
Given a sentence not starting by a uppercase word,
It returns False
"""
def test_given_sentence_with_no_valid_start_but_valid_ending():
    grammar_checker = text_checker("are you a superhero?")
    assert grammar_checker == False


"""
Given a sentence not starting with a capital letter and not ending with any punctuation mark.
It returns False
"""
def test_given_sentence_with_no_valid_start_and_ending():
    grammar_checker = text_checker("oh, my god, you are a pirate") 
    assert grammar_checker == False
