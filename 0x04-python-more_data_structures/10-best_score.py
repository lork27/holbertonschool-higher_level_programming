#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        return list(sorted(a_dictionary.keys()))[-1]
