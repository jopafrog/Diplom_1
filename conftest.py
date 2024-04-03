import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, 'Ingredient1', 100)
    ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, 'Ingredient2', 100)

    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    return burger
