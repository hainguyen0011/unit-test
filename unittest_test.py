from quadratic_equation import *
import unittest


class TestQuadraticEquation(unittest.TestCase):
    def test_delta_cal(self):
        self.assertEqual(delta_calculator(6, 4, -4), 112)
        self.assertEqual(delta_calculator(4, 8, 4), 0)
        self.assertEqual(delta_calculator(7, 2, 4), -108)

    def test_solve_statement(self):
        self.assertEqual(solve(2, 2, 36), (1, -2))
        self.assertEqual(solve(2, 4, 0), (-1))
        self.assertEqual(solve(2, 4, -16), (-1, 1))

    def test_solve_branch(self):
        self.assertEqual(solve(4, 4, 16), (0, -1))
        self.assertEqual(solve(3, 6, 0), (-1))
        self.assertEqual(solve(8, 0, -64), (0, 0.5))


if __name__ == '__main__':
    unittest.main()
