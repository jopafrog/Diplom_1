from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:
    def test_set_buns_correct_creation(self):
        bun = Bun('TestNameBun', 100)
        burger = Burger()

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_one_ingredient_correct_add(self):
        burger = Burger()
        ingredient = Ingredient('tipe', 'TestIngredientName', 100)

        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_remove_ingredient_correct_index_success_remove(self):
        burger = Burger()
        ingredient1 = Ingredient('tipe1', 'Ingredient1', 100)
        ingredient2 = Ingredient('tipe2', 'Ingredient2', 100)

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(0)

        assert ingredient2 in burger.ingredients and ingredient1 not in burger.ingredients

    def test_move_ingredient_success_move(self):
        burger = Burger()
        ingredient1 = Ingredient('tipe1', 'Ingredient1', 100)
        ingredient2 = Ingredient('tipe2', 'Ingredient2', 100)

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == ingredient2 and burger.ingredients[1] == ingredient1

    def test_get_price_success(self):
        burger = Burger()
        bun = Bun('TestNameBun', 100)  # X2 к стоимости
        ingredient1 = Ingredient('tipe1', 'Ingredient1', 100)
        ingredient2 = Ingredient('tipe2', 'Ingredient2', 100)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        assert burger.get_price() == 400

    def test_get_receipt_success(self):
        burger = Burger()
        bun = Bun('BunDefault', 100)  # X2 к стоимости
        ingredient1 = Ingredient('tipe1', 'Ingredient1', 100)
        ingredient2 = Ingredient('tipe2', 'Ingredient2', 100)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        assert 'Price: 400' in burger.get_receipt()

