#!/usr/bin/python3
def multiple_returns(sentence):
    lenSentence = len(sentence)

    if (lenSentence == 0):
        new_tuple = (lenSentence, None)
    else:
        new_tuple = (lenSentence, sentence[0])

    return (new_tuple)
