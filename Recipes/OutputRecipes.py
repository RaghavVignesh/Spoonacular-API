class OutputRecipes:
    def __init__(self, user_missing_items=[], user_missing_items_aisles={}, user_missing_ingredients_prices={}):
        self.user_missing_items = user_missing_items
        self.user_missing_items_aisles = user_missing_items_aisles
        self.missing_items_prices = user_missing_ingredients_prices


def process_output_to_user(missing_items, user_missing_items_aisle, user_missing_items_price):
    print("showing you the missing items")
    if all(x is None for x in missing_items):
        raise ValueError("You have not liked any recipes and you do not have any missing items.")
    total_price = 0.0
    for item in missing_items:
        aisle = user_missing_items_aisle[item]
        price = user_missing_items_price[item]
        total_price += price
        print("You will need to shop %s and you can find this in the %s aisle and it will cost you %s $" % (
            item, aisle, price))

    print("All the items will totally cost you %s $" % total_price)
