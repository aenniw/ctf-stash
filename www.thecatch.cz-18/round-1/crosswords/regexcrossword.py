#!/usr/bin/env python3

"""
####  
# Taken from https://github.com/antoine-trux/regex-crossword-solver
# All credit should go to original author
# 
# - Changed 'xrange' to 'range' in this file to make it python3 compatible.
# - Added python3 shebang
#
####

A program to solve regular expression crosswords like those from
http://regexcrossword.com/
"""

import regex as re


class Crossword(object):
    """
    The crossword puzzle

    The width and height index begins in the upper left hand corner
    """

    # represents all the available characters for this puzzle
    possibility = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890'

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.regexes = dict(
            [('{}A'.format(index), [])
                for index in range(1, self.height + 1)]
            +
            [('{}D'.format(index), [])
                for index in range(1, self.width + 1)]
        )
        self.solutions = ['' for _ in range(self.width * self.height)]
        self.set_possibility(self.possibility)

    def set_possibility(self, string):
        """
        Replaces the current value of self.possibility with `string`
        """
        self.possibility = string
        self.possibilities = [self.possibility
                for _ in range(self.width * self.height)]

    def add_to_possibility(self, string):
        """
        For those puzzles that use more than just letters and numbers, add the
        extra values to the possibilities
        """
        self.possibility += string
        self.possibilities = [self.possibility
                for _ in range(self.width * self.height)]

    def remove_from_possibility(self, string):
        for letter in string:
            if letter in self.possibility:
                self.possibility = self.possibility.replace(letter, '')
        self.possibilities = [self.possibility
                for _ in range(self.width * self.height)]

    def add_regex(self, index, direction, regex):
        """
        Given the index and direction (Across or Down), add the regex to
        self.regexes
        """
        if direction not in ['A', 'D']:
            raise ValueError('{} is not A or D'.format(direction))
        elif index <= 0:
            raise ValueError('Index cannot be less than 0')
        elif direction == 'D' and index > self.width:
            raise ValueError('Index cannot be greater than width')
        elif direction == 'A' and index > self.height:
            raise ValueError('Index cannot be greater than height')
        self.regexes['{}{}'.format(index, direction)].append(regex)

    def solve(self, return_all=False):
        """
        Solve the puzzle and return the results as a string. Results represent
        the answers read from left to right, as when reading a book.

        Uses the Backtracking algoritm
        https://en.wikipedia.org/wiki/Backtracking

            select next available for this spot from the available list
            if matches:
                if last spot:
                    yay!
                else:
                    go to next spot
            if doesn't match:
                set this spot back to all possibilities
                go back to previous spot

        Recursion was attempted first, but python's maximum recursion depth was
        hit after trying to solve a 5x5 puzzle. A while loop is being used
        instead.

        Optional arg `return_all` when set to True means this method will
        return a list of all possible solutions, else, only the first found
        solution is returned.
        """
        index = 0
        sols = []
        while True:
            if index < 0:
                if return_all:
                    return sols
                raise UnsolvableError('Puzzle is unsolvable!')
            elif not self.possibilities[index]:
                self.solutions[index] = ''
                self.possibilities[index] = self.possibility
                index -= 1
                continue

            self.solutions[index] = self.possibilities[index][-1]
            self.possibilities[index] = self.possibilities[index][:-1]
            if self._check_fuzzy_solution():
                if self._is_solved():
                    this_sol = ''.join(self.solutions)
                    if not return_all:
                        return this_sol
                    sols.append(this_sol)
                    continue
                index += 1
            else:
                if not self.possibilities[index]:
                    self.solutions[index] = ''
                    self.possibilities[index] = self.possibility
                    index -= 1

    def _check_fuzzy_solution(self):
        """
        Return True if the current values in self.solution returns a fuzzy
        match for all rows/columns
        """
        # confirm all rows
        for row_index in range(1, self.height + 1):
            row_str = ''.join(self._get_solutions_for_row(row_index))
            row_regexes = self.regexes['{}A'.format(row_index)]
            for regex in row_regexes:
                if not is_fuzzy_match(row_str, regex, max_length=self.width):
                    return False

        # confirm all columns
        for col_index in range(1, self.width + 1):
            col_str = ''.join(self._get_solutions_for_col(col_index))
            col_regexes = self.regexes['{}D'.format(col_index)]
            for regex in col_regexes:
                if not is_fuzzy_match(col_str, regex, max_length=self.height):
                    return False

        return True

    def _get_solutions_for_row(self, index):
        """
        Given an integer for the index, return the current solutions for that
        row
        """
        if index < 0:
            raise ValueError('Index cannot be less than 0')
        elif index > self.height:
            raise ValueError(
                'Index cannot be larger than the height of the crossword')

        begin = self.width * (index - 1)
        end = begin + self.width
        return self.solutions[begin:end]

    def _get_solutions_for_col(self, index):
        """
        Given an integer for the index, return the current solutions for that
        column
        """
        if index < 0:
            raise ValueError('Index cannot be less than 0')
        elif index > self.width:
            raise ValueError(
                'Index cannot be larger than the width of the crossword')

        begin = index - 1
        interval = self.width
        return self.solutions[begin::interval]

    def _is_solved(self):
        """
        Return True if all elements of self.solution have values (a space is
        considered a value)
        """
        return all(self.solutions)


def is_fuzzy_match(string, regex, max_length=None):
    """
    Given a string and a regular expression, return True if the string matches
    the beginning of the regex.

    For example, if string = 'A' and regex = 'A{3}', returns True because what
    is given of the string would match the regular expression.

    However, if string = 'B' and regex = 'A{3}', then return False.
    """
    partial = len(string) != max_length

    pattern = re.compile(regex)
    if pattern.fullmatch(string, partial=partial):
        return True
    return False


class UnsolvableError(Exception):
    pass
