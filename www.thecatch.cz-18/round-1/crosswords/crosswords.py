#!/usr/bin/env python3

import re
from regexcrossword import Crossword

# Example for various reasons:
def test_solve_2x2():
    # from http://regexcrossword.com/challenges/beginner/puzzles/1
    crossword = Crossword(2, 2)
    
    # "A" means across
    crossword.add_regex(1, 'A', 'HE|LL|O+')
    crossword.add_regex(2, 'A', '[PLEASE]+')

    # "D" means down
    crossword.add_regex(1, 'D', '[^SPEAK]+')
    crossword.add_regex(2, 'D', 'EP|IP|EF')
    print(crossword.solve())


def solve_THECATCH18():
    crossword = Crossword(5, 5)
    
    # Need to add "-" to possible characters
    # because crossword class by default assumes only:
    # - [A-Z]
    # - [0-9]
    # - :space:
    crossword.add_to_possibility('-')

    # This crossword does not have standart rectangular shape,
    # but luckily, we know that the flag looks like:
    # CT18-XXXX-XXXX-XXXX-XXXX
    # so we can assume that every character in the last COLUMN will be "-",
    # which is confirmed by its regex "(-)+",
    # so we append "-" also to the last ROW regex '[RTE]+(.)\1',
    # so that we get standard rectangular puzzle solvable by the algorithm
    # and we remove the last dash character afterwards, when printing the flag.
    # Also note the `r` which expands regexes like `\d` to `0123456789`

    # "A" means across
    crossword.add_regex(1, 'A', r'[CA][TB][\dKG-]*')
    crossword.add_regex(2, 'A', r'(KE|RT|TA)*-')
    crossword.add_regex(3, 'A', r'(RE|QR)[QUWST-]*')
    crossword.add_regex(4, 'A', r'[ONW]*S[RITE-]*')
     # This regex has "-" appended to make the puzzle rectangular
    crossword.add_regex(5, 'A', r'[RTE]+(.)\1-')

    # "D" means across
    crossword.add_regex(1, 'D', r'[ABC]T*(.)[MNP]\1')
    crossword.add_regex(2, 'D', r'[ATL]+(.)[OCD]+\1')
    crossword.add_regex(3, 'D', r'[HAKS1]*([SAP])\1')
    crossword.add_regex(4, 'D', r'(4W|1D|8E)T*S+')
    crossword.add_regex(5, 'D', r'(-)+')
    
    print(crossword.solve()[:-1]) # Printing the flag without the last dash.

# test_solve_2x2()
solve_THECATCH18()
