from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:
    def test_set_buns_correct_creation(self):
        bun = Bun('TestBun', 100)
        burger = Burger()

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_one_ingredient_correct_add(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'TestIngredientName', 100)

        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_remove_ingredient_correct_index_success_remove(self, burger):
        ingredient1 = burger.ingredients[0]
        ingredient2 = burger.ingredients[1]

        burger.remove_ingredient(0)

        assert ingredient2 in burger.ingredients and ingredient1 not in burger.ingredients

    def test_move_ingredient_success_move(self, burger):
        ingredient1 = burger.ingredients[0]
        ingredient2 = burger.ingredients[1]

        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == ingredient2 and burger.ingredients[1] == ingredient1

    def test_get_price_success(self, burger):
        bun = Bun('TestBun', 100)
        burger.set_buns(bun)

        assert burger.get_price() == 400

    def test_get_receipt_success(self, burger):
        bun = Bun('TestBun', 100)
        burger.set_buns(bun)

        assert 'Price: 400' in burger.get_receipt()

