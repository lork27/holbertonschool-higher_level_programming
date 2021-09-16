#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return list(sorted(a_dictionary.keys(), reverse=True))[0]
