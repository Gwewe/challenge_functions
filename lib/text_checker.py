def text_checker(text):
    if text[0].isupper():
        return text[-1] in ".?!"
    else:
        return False