class Ingredient:
    def __init__(self, ingredients=[]):
        self.ingredients = ingredients


def process_ingredients(ingredients):
    result = ''
    if all(x is None for x in ingredients):
        raise ValueError("You have not entered any ingredients")

    # ingredients = ['apples','oranges','bananas']
    for item in ingredients:
        result = result + item + ','

    result = result[:-1]
    return result
