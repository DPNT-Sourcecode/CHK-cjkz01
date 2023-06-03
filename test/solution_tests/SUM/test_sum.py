from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_two(self):
        assert sum_solution.compute(2, 3) == 5

    def test_three(self):
        assert sum_solution.compute(2, 3) > 3


