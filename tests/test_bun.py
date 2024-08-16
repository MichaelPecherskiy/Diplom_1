import pytest
from praktikum.bun import Bun


class TestBun:

    def test_bun(self, mock_bun):
        bun = Bun("булочка", 10.0)
        assert bun.get_name() == mock_bun.get_name()
        assert bun.get_price() == mock_bun.get_price()


    def test_bun_(self):
        bun = Bun("bun", 10.0)
        assert isinstance(bun.get_name(), str)
        assert isinstance(bun.get_price(), float)
