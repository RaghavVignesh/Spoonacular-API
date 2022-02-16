class Ingredient:
    def __init__(self, ingredients=[]):
        self.ingredients = ingredients


''' This method takes the ingredients as a list and converts the list
    into a string which can be used as a parameter for the requests
    module as an input
'''


def process_ingredients(ingredients):
    result = ''
    if all(x is None for x in ingredients):
        raise ValueError("You have not entered any ingredients")

    # ingredients = ['apples','oranges','bananas']
    for item in ingredients:
        result = result + item + ','

    result = result[:-1]
    return result
