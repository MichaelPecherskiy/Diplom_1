import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("expected_name", ["булочка"])
    def test_bun_name(self, expected_name):
        bun = Bun(expected_name, 10.0)
        assert bun.get_name() == expected_name, f"Ожидалось имя '{expected_name}', но получено '{bun.get_name()}'"

    @pytest.mark.parametrize("expected_price", [10.0])
    def test_bun_price(self, expected_price):
        bun = Bun("булочка", expected_price)
        assert bun.get_price() == expected_price, f"Ожидалась цена '{expected_price}', но получена '{bun.get_price()}'"


    def test_bun_(self):
        bun = Bun("bun", 10.0)
        assert isinstance(bun.get_name(), str)
        assert isinstance(bun.get_price(), float)
