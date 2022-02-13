class UserRecipes:
    def __init__(self, recipes=[], missing_ingredients={}, missing_ingredients_aisles={},
                 missing_ingredients_prices={}):
        self.recipes = recipes
        self.missing_ingredients = missing_ingredients
        self.missing_ingredient_aisles = missing_ingredients_aisles
        self.missing_ingredient_prices = missing_ingredients_prices


def process_user_input(recipes, missing_ingredients, missing_ingredient_aisles, missing_ingredient_prices):
    count = 0
    size = len(recipes)
    # print(size)
    user_missing_items_aisles = {}
    user_missing_items_prices = {}
    user_missing_items = []
    while True:
        print("Recipe Suggestion based on the ingredients you entered: " + " " + recipes[count])
        user_input = input("Do you like the recipe?Enter Yes or No")
        if user_input == "Yes":
            missing_items_for_recipe = missing_ingredients[recipes[count]]
            for item in missing_items_for_recipe:
                user_missing_items.append(item)
                user_missing_items_aisles[item] = missing_ingredient_aisles[item]
                if item not in user_missing_items_prices:
                    user_missing_items_prices[item] = missing_ingredient_prices[item]
                else:
                    existing_cost = user_missing_items_prices.get(item)
                    user_missing_items_prices[item] = existing_cost + missing_ingredient_prices[item]
            count = count + 1
            user_shopping_choice = input("Do you want to continue shopping?Enter Yes or No")
            if count >= size:
                print("We have run out of recipes.Please try again")
                break
            elif count < size:
                if user_shopping_choice == "No":
                    print("Thanks for shopping!!")
                    break
                elif user_shopping_choice == "Yes":
                    print("Showing you the next recipe")
                else:
                    print("You have entered an invalid input. Trying again")

        elif user_input == "No":
            print("Showing you a new recipe")
            count = count + 1
            if count >= size:
                print("We have run out of recipes.Please try again")
                break
        else:
            print("You have entered an invalid input.Try again")
            pass

    return user_missing_items, user_missing_items_aisles, user_missing_items_prices
