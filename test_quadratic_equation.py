from quadratic_equation import *
import pytest


@pytest.mark.delta
@pytest.mark.parametrize("a,b,c,output",
                         [(6, 4, -4, 112),
                          (4, 8, 4, 0),
                          (7, 2, 4, -108)])
def test_delta_calculator(a, b, c, output):
    assert delta_calculator(a, b, c) == output


@pytest.mark.statement_coverage
@pytest.mark.parametrize("a,b,delta,output",
                         [(2, 2, 36, (1, -2)),
                          (2, 4, 0, (-1)),
                          (2, 4, -16, (-1, 1))])
def test_solve_statement(a, b, delta, output):
    assert solve(a, b, delta) == output


@pytest.mark.branch_coverage
@pytest.mark.parametrize("a,b,delta,output",
                         [(4, 4, 16, (-1, 0)),
                          (3, 6, 0, (-1)),
                          (8, 0, -64, (0, 0.5))])
def test_solve_branch(a, b, delta, output):
    assert solve(a, b, delta) == output