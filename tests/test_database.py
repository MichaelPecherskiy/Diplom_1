import pytest
from praktikum.database import Database


class TestDatabase:

    @pytest.mark.parametrize("expected_bun_count, expected_ingredient_count", [
        (3, 6),
    ])
    def test_available_buns_and_ingredients(self, expected_bun_count, expected_ingredient_count, mock_database):
        db = mock_database
        buns = db.available_buns()
        assert len(
            buns) == expected_bun_count, f"Ожидаемое количество булочек: {expected_bun_count}, найдено: {len(buns)}"
        ingredients = db.available_ingredients()
        assert len(
            ingredients) == expected_ingredient_count, f"Ожидаемое количество ингредиентов: {expected_ingredient_count}," \
                                                       f" найдено: {len(ingredients)}"

    def test_ingredient_addition(self, mock_ingredient_sauce, mock_ingredient_filling):
        db = Database()
        db.ingredients.append(mock_ingredient_sauce)
        db.ingredients.append(mock_ingredient_filling)
        assert mock_ingredient_sauce in db.ingredients, "Соус добавлен в базу данных"
        assert mock_ingredient_filling in db.ingredients, "Филлинг  добавлен в базу данных"


        # Проверка, что добавленные ингредиенты имеют правильные тип, название и цену
        last_added_ingredient = db.ingredients[-2]
        assert last_added_ingredient.get_type() == mock_ingredient_sauce.get_type(), \
            f"Тип ингредиента{mock_ingredient_sauce.get_type()}"
        assert last_added_ingredient.get_name() == mock_ingredient_sauce.get_name(), \
            f"Название ингредиента {mock_ingredient_sauce.get_name()}"
        assert last_added_ingredient.get_price() == mock_ingredient_sauce.get_price(), \
            f"Цена ингредиента{mock_ingredient_sauce.get_price()}"

        last_added_ingredient = db.ingredients[-1]
        assert last_added_ingredient.get_type() == mock_ingredient_filling.get_type(), \
            f"Тип ингредиента  {mock_ingredient_filling.get_type()}"
        assert last_added_ingredient.get_name() == mock_ingredient_filling.get_name(), \
            f"Название ингредиента  {mock_ingredient_filling.get_name()}"
        assert last_added_ingredient.get_price() == mock_ingredient_filling.get_price(), \
            f"Цена ингредиента {mock_ingredient_filling.get_price()}"

