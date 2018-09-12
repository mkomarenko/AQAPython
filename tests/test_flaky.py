from random import choice

import pytest


class TestFlaky:
    @pytest.mark.flaky(reruns=2)
    def test_random(self):
        assert choice([True, False])
