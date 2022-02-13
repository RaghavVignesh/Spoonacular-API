import unittest
from APIService import APIService
from Ingredients import Ingredients
from Recipes import Recipes
from TestResponseData import response_data


class TestUtils(unittest.TestCase):
    def test_call_spoonacular_api(self):
        ingredient_list = ['bananas']
        response_data_new = APIService.call_spoonacular_api(ingredient_list)
        self.assertTrue(response_data_new is not None)

    def test_call_spoonacular_api_response_size(self):
        ingredient_list = ['bananas']
        response_data_new = APIService.call_spoonacular_api(ingredient_list)
        self.assertTrue(len(response_data_new) == 20)

    def test_call_spoonacular_api_invalid_ingredient(self):
        ingredient_list = ['cringes']
        with self.assertRaises(Exception) as context:
            APIService.call_spoonacular_api(ingredient_list)
            self.assertTrue(
                'There are no recipes for the ingredients you requested. Please try with different ingredients.' in str
                (context.exception))

    def test_process_ingredients_test_one(self):
        ingredient_list = ['apples,oranges']
        final_ingredients = Ingredients.process_ingredients(ingredient_list)
        self.assertTrue(final_ingredients == 'apples,oranges')

    def test_process_ingredients_test_two(self):
        ingredient_list = ['bananas', 'grapes', 'lime']
        final_ingredients = Ingredients.process_ingredients(ingredient_list)
        self.assertTrue(final_ingredients == 'bananas,grapes,lime')

    def test_process_recipes(self):
        recipes, missing_ingredients, missing_ingredients_aisles, missing_ingredients_prices = Recipes.process_recipes(
            response_data)
        self.assertTrue(recipes == ['beetroot apple smoothie'])

    def test_process_recipes_missing_ingredients(self):
        recipes, missing_ingredients, missing_ingredients_aisles, missing_ingredients_prices = Recipes.process_recipes(
            response_data)
        final_missing_ingredients = []
        for values in missing_ingredients.values():
            final_missing_ingredients.append(values)

        self.assertTrue(final_missing_ingredients == [['beetroot', 'pear']])

    def test_process_recipes_missing_ingredients_aisles(self):
        recipes, missing_ingredients, missing_ingredients_aisles, missing_ingredients_prices = Recipes.process_recipes(
            response_data)
        final_missing_ingredients_aisles = []
        for values in missing_ingredients_aisles.values():
            final_missing_ingredients_aisles.append(values)

        print(final_missing_ingredients_aisles)
        self.assertTrue(final_missing_ingredients_aisles == ['Produce', 'Produce'])

    def test_process_recipes_missing_ingredients_prices(self):
        recipes, missing_ingredients, missing_ingredients_aisles, missing_ingredients_prices = Recipes.process_recipes(
            response_data)
        final_missing_ingredients_prices = []
        for values in missing_ingredients_prices.values():
            final_missing_ingredients_prices.append(values)

        print(final_missing_ingredients_prices)
        self.assertTrue(final_missing_ingredients_prices == [0.5, 1.0])


if __name__ == '__main__':
    unittest.main()
