from solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("ABCDE") == 155
        assert checkout_solution.checkout("E") == 40

    # def test_two(self):
    #     assert sum_solution.compute(2, 3) == 5
    #
    # def test_three(self):
    #     assert sum_solution.compute(2, 3) > 3


