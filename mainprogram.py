import argparse
from Ingredients import Ingredients
from APIService import APIService
from Recipes import Recipes
from Recipes import UserRecipes
from Recipes import OutputRecipes

''' This is the main method that drives the program.
    We parse the command line arguments and extract ingredients
    from the command line arguments. We then get all the missing ingredients
    for the recipes and store their aisles and their prices and display the
     prices to the user.
'''


def main():
    print("Welcome to the SPOONACULAR API Project")
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--ingredients', nargs='+', default=[])
    args = parser.parse_args()
    ingredient_list = args.ingredients
    final_ingredients = Ingredients.process_ingredients(ingredient_list)
    response_data = APIService.call_spoonacular_api(final_ingredients)
    recipes, missing_ingredients, missing_ingredients_aisles, missing_ingredients_prices = Recipes.process_recipes(
        response_data)
    user_missing_items, user_missing_items_aisles, user_missing_items_prices = UserRecipes.process_user_input(recipes,
                                                                                                              missing_ingredients,
                                                                                                              missing_ingredients_aisles,
                                                                                                              missing_ingredients_prices)
    OutputRecipes.process_output_to_user(user_missing_items, user_missing_items_aisles, user_missing_items_prices)


if __name__ == "__main__":
    main()
