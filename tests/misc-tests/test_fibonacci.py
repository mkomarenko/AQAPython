import allure
import pytest

from src.fibonacci import fib


@pytest.mark.misc_test
class TestFibonacci:

    @allure.title("Fibonacci series for '10'")
    def test_fib_ten(self):
        assert fib(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    @allure.title("Fibonacci series for '0'")
    def test_fib_zero(self):
        assert fib(0) == []

    @allure.title("Fibonacci series for '1'")
    def test_fib_one(self):
        assert fib(1) == [0]

    @allure.title("Fibonacci series negative")
    def test_fib_negative(self):
        assert fib(-1) == []
