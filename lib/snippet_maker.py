def snippet_maker(text):
    list()
    text_split = text.split(" ")
    if len(text_split) > 5:
        first_five_words = text_split[:5]
        snippet = " ".join(first_five_words)
        return snippet + "..."
    else:
        return text