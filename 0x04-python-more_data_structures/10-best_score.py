#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    new={v:k for k,v in a_dictionary.items()}
    return new[max(new)]
