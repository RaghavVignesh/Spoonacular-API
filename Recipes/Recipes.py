class Recipe:
    def __init__(self, response_data=[]):
        self.response_data = response_data


def process_recipes(response_data):
    recipes = []
    missing_ingredients = {}
    missing_ingredients_aisles = {}
    missing_ingredients_prices = {}
    for item in response_data:
        # print(item)
        recipe = item["title"]
        recipes.append(recipe)
        missing_items = []
        missing_ingredient = item["missedIngredients"]
        for missing_ingredient_item in missing_ingredient:
            missing_item = missing_ingredient_item["name"]
            aisle = missing_ingredient_item["aisle"]
            price = missing_ingredient_item["amount"]
            missing_ingredients_aisles[missing_item] = aisle
            missing_ingredients_prices[missing_item] = price
            missing_items.append(missing_item)
        missing_ingredients[recipe] = missing_items

    return recipes,missing_ingredients,missing_ingredients_aisles,missing_ingredients_prices
