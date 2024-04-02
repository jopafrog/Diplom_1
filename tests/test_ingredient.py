from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price_correct_price_success(self):
        ingredient = Ingredient('tipe', 'TestIngredientName', 100)

        assert ingredient.get_price() == 100

    def test_get_name_correct_name_success(self):
        ingredient = Ingredient('tipe', 'TestIngredientName', 100)

        assert ingredient.get_name() == 'TestIngredientName'

    def test_get_type_correct_type_success(self):
        ingredient = Ingredient('tipe', 'TestIngredientName', 100)

        assert ingredient.get_type() == 'tipe'
