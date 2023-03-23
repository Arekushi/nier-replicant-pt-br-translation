def group_phrases(phrases, limit):
    sublist = []
    length = 0

    for index, phrase in enumerate(phrases):
        phrase = str(phrase)

        if length + len(phrase) > limit and sublist:
            yield sublist
            sublist = []
            length = 0
        sublist.append((index, phrase))
        length += len(phrase)

    if sublist:
        yield sublist
