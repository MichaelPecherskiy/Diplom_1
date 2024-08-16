import pytest
from praktikum.bun import Bun
from unittest.mock import MagicMock
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING



@pytest.fixture
def mock_bun():
    mock = MagicMock(spec=Bun)
    mock.get_name.return_value = "булочка"
    mock.get_price.return_value = 10.0
    return mock


@pytest.fixture
def mock_ingredient():
    mock = MagicMock(spec=Ingredient)
    mock.get_name.return_value = "test_ingridient"
    mock.get_price.return_value = 100.0
    mock.get_type.return_value = "test_type"
    return mock


@pytest.fixture
def expected_receipt():
    return "(==== булочка ====)\n= test_type test_ingridient =\n(==== булочка ====)\n\nPrice: 120.0"


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_ingredient_sauce():
    mock_ingredient = MagicMock(spec=Ingredient)
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_ingredient.get_name.return_value = "hot sauce"
    mock_ingredient.get_price.return_value = 100
    return mock_ingredient


@pytest.fixture
def mock_ingredient_filling():
    mock_ingredient = MagicMock(spec=Ingredient)
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_ingredient.get_name.return_value = "cutlet"
    mock_ingredient.get_price.return_value = 100
    return mock_ingredient


@pytest.fixture
def mock_database():
    return Database()
