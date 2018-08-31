from .fibonacci import fib


class TestFibonacci:

    def test_fib_ten(self):
        assert fib(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_fib_zero(self):
        assert fib(0) == []

    def test_fib_one(self):
        assert fib(1) == [0]

    def test_fib_negative(self):
        assert fib(-1) == []
