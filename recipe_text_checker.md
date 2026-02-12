# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe_text_checker.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

```python
## User Story
- As a user
- So that I can improve my grammar
- I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

> Clarification needed on whether it is multiple sentence or just one.
> As we do not have the clarification, we will ignore any additional sentences.
```

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def text_checker(text):
    """Confirm that text start with uppercase word and end with a suitable sentence-ending punctuation mark

    Parameters: (list all parameters and their types)
        text: a string containing text (e.g. "Hello, my name is Wewe.")

    Returns: (state the return value and its type)
        Boolean true or false if the text is correctly punctuated (e.g. "Hello, my name is Wewe.")

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

# """
# Given a sentence starting with an uppercase word and ending with a dot
# It returns True
# """
# text_checker("Hello, Bruce Wayne.") => True

# """
# Given a sentence starting with an uppercase and ending with a question mark,
# It returns True
# """
# text_checker("Are you a superhero?") => True

# """
# Given a sentence starting with an uppercase and ending with a exclamation mark,
# It returns True
# """
# text_checker("You are a superhero!") => True

# """
# Given a sentence not starting by a uppercase word,
# It returns False
# """
# text_checker("are you a superhero?") => False

# """
# Given a sentence not starting with a capital letter and not ending with any punctuation mark.
# It returns False
# """
# text_checker("oh, my god, you are a pirate") => False

# """
# Given a sentence starting with capital letter but ending with colons.
# It returns False
# """
# text_checker("Oh, my god, you are a pirate:") => False

# """
# Given a sentence starting with capital letter but ending with comma.
# It returns False
# """
# text_checker("Oh, my god, you are a pirate,") => False

# """
# Given a sentence not starting or ending with the proper conditions.
# It returns False
# """
# text_checker("oh, your name is luffy") => False
"""
Given a empty sentence
It throws an error
"""
text_checker("") throws an error
# Raises "Cannot check grammar of an empty string
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
