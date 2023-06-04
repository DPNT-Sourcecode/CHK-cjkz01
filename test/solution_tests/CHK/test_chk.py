from solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("ABCDE") == 155
        assert checkout_solution.checkout("E") == 40

    def test_two(self):
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EEEB") == 120
        assert checkout_solution.checkout("EEEEBB") == 160

    def test_three(self):
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("BBB") == 75
        assert checkout_solution.checkout("BBBB") == 90

    #
    # def test_three(self):
    #     assert sum_solution.compute(2, 3) > 3
