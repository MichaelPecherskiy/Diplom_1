import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price, expected_type, expected_name, expected_price", [
        (INGREDIENT_TYPE_FILLING, "помидор", 10.0, INGREDIENT_TYPE_FILLING, "помидор", 10.0),
        (INGREDIENT_TYPE_SAUCE, "сырный", 5.0, INGREDIENT_TYPE_SAUCE, "сырный", 5.0),
        (INGREDIENT_TYPE_FILLING, "лук", 9.0, INGREDIENT_TYPE_FILLING, "лук", 9.0),
    ])
    def test_ingredient_attributes(self, ingredient_type, name, price, expected_type, expected_name, expected_price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert isinstance(ingredient_type, str)
        assert isinstance(name, str)
        assert isinstance(price, float)

        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price
