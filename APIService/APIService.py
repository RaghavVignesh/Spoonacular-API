from Main import config;
import requests


class APIService:

    def __init__(self, ingredemt_list=[]):
        self.ingredient_list = ingredemt_list


def call_spoonacular_api(ingredient_list):
    end_point = "https://api.spoonacular.com/recipes/findByIngredients"
    api_secret_key = config.api_secret_key
    payload = {
        'ingredients': ingredient_list,
        'apiKey': api_secret_key,
        'number': 20
    }
    response = call_api(end_point, payload)
    # response = requests.get(end_point, params=payload)
    response_data = response.json()
    if not response_data:
        raise ValueError(
            "There are no recipes for the ingredients you requested. Please try with different ingredients.")

    return response_data


def call_api(end_point, payload):
    try:
        response = requests.get(end_point, params=payload, timeout=3)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print("There is an error in making the request and the error is:", error)
    except requests.exceptions.HTTPError as error:
        print("Request Failed with Http Error:", error)
    except requests.exceptions.ConnectionError as error:
        print("Request Failed with Connection Error", error)
    except requests.exceptions.Timeout as error:
        print("Request Failed with Timeout Error", error)
    except requests.exceptions.InvalidURL as error:
        print("The Request URL is invalid", error)
    except requests.exceptions.ContentDecodingError as error:
        print("There is an error in decoding the response json", error)

    return response



