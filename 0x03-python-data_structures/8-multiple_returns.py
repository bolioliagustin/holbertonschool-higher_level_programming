#!/usr/bin/python3
def multiple_returns(sentence):
    i = len(sentence)
    if sentence == '':
        return (i, None)
    else:
        a = sentence[0]
        return(i, a)
