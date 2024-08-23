

class TestBurger:
    """тест проверяет создание булочки"""


    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    """тест добавляет ингредиент в список ингредиентов бургера"""


    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]


    """тест удаляет ингредиент из списка"""


    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        initial_count = len(burger.ingredients)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == initial_count - 1


    """тест перемещает ингредиент в списке с одного места на другое"""


    def test_move_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient, mock_ingredient]


    """тест  рассчитывает общую стоимость бургера"""


    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 220.0


    "тест формирует рецепт с информацией о бургере"""

    def test_get_receipt(self, burger, mock_bun, mock_ingredient, expected_receipt):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert receipt == expected_receipt, f"Ожидался рецепт '{expected_receipt}', но получен '{receipt}'"

    def test_bun_in_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert mock_bun.get_name() in receipt, f"Имя булочки '{mock_bun.get_name()}' отсутствует в рецепте"

    def test_ingredient_in_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        expected_ingredient_text = f"= {str(mock_ingredient.get_type()).lower()} {mock_ingredient.get_name()} ="
        assert expected_ingredient_text in receipt, f"Ингредиент '{expected_ingredient_text}' отсутствует в рецепте"

    def test_price_in_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        expected_price_text = f"Price: {burger.get_price()}"
        assert expected_price_text in receipt, f"Цена '{expected_price_text}' отсутствует в рецепте"
