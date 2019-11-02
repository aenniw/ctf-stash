import unittest

from regexcrossword import Crossword, is_fuzzy_match, UnsolvableError


class TestCrossword(unittest.TestCase):

    def test_init_solutions(self):
        cw = Crossword(2, 2)
        self.assertEqual(cw.solutions, ['', '', '', ''])
        cw = Crossword(3, 3)
        self.assertEqual(cw.solutions, ['', '', '', '', '', '', '', '', ''])

    def test_is_solved(self):
        cw = Crossword(2, 2)
        self.assertFalse(cw._is_solved())
        cw.solutions = ['A', 'A', 'A', 'A']
        self.assertTrue(cw._is_solved())
        cw.solutions = ['A', '', 'A', '']
        self.assertFalse(cw._is_solved())
        cw.solutions = ['A', ' ', 'B']
        self.assertTrue(cw._is_solved())

    def test_init_regexes(self):
        cw = Crossword(2, 2)
        self.assertDictEqual(
            cw.regexes,
            {'1A': [], '2A': [], '1D': [], '2D': []}
        )

    def test_get_solutions_for_row(self):
        cw = Crossword(2, 2)
        cw.solutions = ['A', 'B', 'C', 'D']
        self.assertEqual(
            cw._get_solutions_for_row(1),
            ['A', 'B']
        )
        self.assertEqual(
            cw._get_solutions_for_row(2),
            ['C', 'D']
        )
        cw = Crossword(3, 3)
        cw.solutions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.assertEqual(
            cw._get_solutions_for_row(1),
            ['A', 'B', 'C']
        )
        self.assertEqual(
            cw._get_solutions_for_row(2),
            ['D', 'E', 'F']
        )

    def test_get_solutions_for_col(self):
        cw = Crossword(2, 2)
        cw.solutions = ['A', 'B', 'C', 'D']
        self.assertEqual(
            cw._get_solutions_for_col(1),
            ['A', 'C']
        )
        self.assertEqual(
            cw._get_solutions_for_col(2),
            ['B', 'D']
        )
        cw = Crossword(3, 3)
        cw.solutions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.assertEqual(
            cw._get_solutions_for_col(1),
            ['A', 'D', 'G']
        )
        self.assertEqual(
            cw._get_solutions_for_col(2),
            ['B', 'E', 'H']
        )

    def test_solve_2x2(self):
        # from http://regexcrossword.com/challenges/beginner/puzzles/1
        crossword = Crossword(2, 2)
        crossword.add_regex(1, 'A', 'HE|LL|O+')
        crossword.add_regex(2, 'A', '[PLEASE]+')
        crossword.add_regex(1, 'D', '[^SPEAK]+')
        crossword.add_regex(2, 'D', 'EP|IP|EF')
        self.assertEqual(crossword.solve(), 'HELP')

    def test_solve_1x2(self):
        # from http://regexcrossword.com/challenges/tutorial/puzzles/4
        crossword = Crossword(1, 2)
        crossword.add_regex(1, 'A', 'A')
        crossword.add_regex(2, 'A', 'AB*')
        crossword.add_regex(1, 'D', 'A*')
        self.assertEqual(crossword.solve(), 'AA')

    def test_solve_4x3(self):
        # from http://regexcrossword.com/playerpuzzles/edfb2756-41e9-4aca-a706-abe640d8c71e
        cw = Crossword(4, 3)

        cw.add_regex(1, 'A', '[MELT]+.[JERK]+')
        cw.add_regex(2, 'A', '[AND]+.K')
        cw.add_regex(3, 'A', '[HEY!!]+')

        cw.add_regex(1, 'D', '[NOT][RAT]E')
        cw.add_regex(2, 'D', 'H[DRO][^HE!!]')
        cw.add_regex(3, 'D', '[THEN]E!')
        cw.add_regex(4, 'D', '[JUMP].!')

        # the answer includes an !, so this will raise an error
        self.assertRaises(UnsolvableError, cw.solve)  # what's the answer?

        cw.add_to_possibility('!')
        self.assertEqual(cw.solve(), 'THEJADEKEY!!')

    def test_solve_with_backreference(self):
        # from http://regexcrossword.com/challenges/tutorial/puzzles/7
        cw = Crossword(1, 2)
        cw.add_regex(1, 'A', 'A|B')
        cw.add_regex(2, 'A', 'A|B')
        # if not a raw string, will be interpretted incorrectly
        cw.add_regex(1, 'D', r'(A)\1')

        self.assertEqual(cw.solve(), 'AA')

    def test_solve_two_regexes_per_direction(self):
        # from http://regexcrossword.com/challenges/doublecross/puzzles/1
        cw = Crossword(2, 1)
        cw.add_regex(1, 'A', r'[A-GN-Z]+')
        cw.add_regex(1, 'A', r'[^A-DI-S]+')
        cw.add_regex(1, 'D', r'[D-HJ-M]')
        cw.add_regex(1, 'D', r'[^F-KM-Z]')
        cw.add_regex(2, 'D', r'[^A-RU-Z]')
        cw.add_regex(2, 'D', r'[A-KS-V]')

        self.assertEqual(cw.solve(), 'ET')

    def test_solve_answer_with_spaces(self):
        cw = Crossword(1, 1)
        cw.add_regex(1, 'A', r'\s')
        self.assertEqual(cw.solve(), ' ')

        cw = Crossword(1, 1)
        cw.add_regex(1, 'A', r'\W')
        self.assertEqual(cw.solve(), ' ')

        # from http://regexcrossword.com/playerpuzzles/f2a55cca-37fe-42e1-967a-56b97e1fc612
        cw = Crossword(5, 3)
        cw.remove_from_possibility('1234567890')
        cw.add_regex(1, 'A', r'[PDA][PAPER]*[PD]A')
        cw.add_regex(2, 'A', r'R[^RA]\s(R.|.R)')
        cw.add_regex(3, 'A', r'\W.NU[\\S]')
        cw.add_regex(1, 'D', r'[O-T]{2}\s?')
        cw.add_regex(2, 'D', r'[^PEA][ARE]A')
        cw.add_regex(3, 'D', r'(HE|F\s|E\s).')
        cw.add_regex(4, 'D', r'[PFCG](.)\1')
        cw.add_regex(5, 'D', r'([CA])RS')
        # this solution is offensive and I do not condone it
        self.assertEqual(cw.solve(), 'PREPARE UR ANUS')

    def test_solve_2x2_with_doubles(self):
        # http://regexcrossword.com/challenges/cities/puzzles/1
        cw = Crossword(2, 2)
        cw.add_regex(1, 'A', r'[LINE]+')
        cw.add_regex(1, 'A', r'[ISLE]+')
        cw.add_regex(2, 'A', r'[LAM]+')
        cw.add_regex(2, 'A', r'[MALE]+')

        cw.add_regex(1, 'D', r'(MA|LM)')
        cw.add_regex(1, 'D', r'[LAME]*')
        cw.add_regex(2, 'D', r'[^MESH]+')
        cw.add_regex(2, 'D', r'[^LES]+')

        self.assertEqual(cw.solve(), 'LIMA')

    def test_solve_3x3_with_special_chars(self):
        # http://regexcrossword.com/challenges/volapuk/puzzles/2
        cw = Crossword(3, 3)
        cw.add_to_possibility('.\\')
        cw.add_regex(1, 'A', r'(Y|\d|M)+')
        cw.add_regex(1, 'A', r'[^IB][0-3]Y')
        cw.add_regex(2, 'A', r'(.H|P|.P)+')
        cw.add_regex(2, 'A', r'^(P|Y)*(PA|\.H$)')
        cw.add_regex(3, 'A', r'[\dIP\s].+')
        cw.add_regex(3, 'A', r'[PA\\d\d]+')

        cw.add_regex(1, 'D', r'M[\DIP]*')
        cw.add_regex(1, 'D', r'(M|A|P)+')
        cw.add_regex(2, 'D', r'(\\d|\d.)[\\\/B]')
        cw.add_regex(2, 'D', r'[^2O13]\.\\*(A|P)?')
        cw.add_regex(3, 'D', r'(Y$|YH|\d$)+')
        cw.add_regex(3, 'D', r'[HOW2Y]+')

        self.assertEqual(cw.solve(), 'M0YP.HP\\2')


class TestIsFuzzyMatch(unittest.TestCase):

    def test_true(self):
        regex = 'AAA'
        self.assertTrue(is_fuzzy_match('A', regex))
        self.assertTrue(is_fuzzy_match('AA', regex))
        self.assertTrue(is_fuzzy_match('AAA', regex))
        regex = 'A{3}'
        self.assertTrue(is_fuzzy_match('A', regex))
        self.assertTrue(is_fuzzy_match('AA', regex))
        self.assertTrue(is_fuzzy_match('AAA', regex))
        regex = 'A\sA'
        self.assertTrue(is_fuzzy_match('A', regex))
        self.assertTrue(is_fuzzy_match('A ', regex))
        self.assertTrue(is_fuzzy_match('A A', regex))
        regex = 'AA\.'
        self.assertTrue(is_fuzzy_match('A', regex))
        self.assertTrue(is_fuzzy_match('AA', regex))
        self.assertTrue(is_fuzzy_match('AA.', regex))
        regex = '[^ABC]{3}'
        self.assertTrue(is_fuzzy_match('X', regex))
        self.assertTrue(is_fuzzy_match('XX', regex))
        self.assertTrue(is_fuzzy_match('XXX', regex))

    def test_false(self):
        regex = 'AAA'
        self.assertFalse(is_fuzzy_match('B', regex))
        self.assertFalse(is_fuzzy_match('BB', regex))
        self.assertFalse(is_fuzzy_match('BBB', regex))
        self.assertFalse(is_fuzzy_match('AB', regex))
        self.assertFalse(is_fuzzy_match('BA', regex))
        self.assertFalse(is_fuzzy_match('AAB', regex))
        regex = 'A{3}'
        self.assertFalse(is_fuzzy_match('B', regex))
        self.assertFalse(is_fuzzy_match('BB', regex))
        self.assertFalse(is_fuzzy_match('BBB', regex))
        regex = '[^ABC]{3}'
        self.assertFalse(is_fuzzy_match('B', regex))
        self.assertFalse(is_fuzzy_match('XXA', regex))
        self.assertFalse(is_fuzzy_match('AXX', regex))
        self.assertFalse(is_fuzzy_match('ABC', regex))

    def test_max_length(self):
        regex = r'A+B'
        self.assertFalse(is_fuzzy_match('AA', regex, max_length=2))
        self.assertTrue(is_fuzzy_match('AB', regex, max_length=2))
        self.assertTrue(is_fuzzy_match('A', regex, max_length=2))


if __name__ == '__main__':
    unittest.main()
