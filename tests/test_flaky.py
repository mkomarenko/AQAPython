from random import choice

import allure
import pytest


@pytest.mark.misc_test
class TestFlaky:
    @allure.title("Flaky random test")
    @pytest.mark.flaky(reruns=2)
    def test_random(self):
        with allure.step("Assert choice"):
            assert choice([True, False])
