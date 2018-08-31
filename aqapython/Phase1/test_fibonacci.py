from .fibonacci import fib


class TestFibonacci:

    def test_fib(self):
        assert fib(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 346]
