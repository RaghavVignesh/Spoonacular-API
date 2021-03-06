                     SPOONACULAR API - DETAILED TECHNICAL DOCUMENTATION FOR DEVELOPERS.

This is a technical documentation about the Spoonacular Project for IRobot Take Home test. It contains a detailed description of the project.

This project is built using Python 3.9.6 as it is the latest version of Python and it is also compatible with Python 3.8. For dependency management, pip(Python Installer Packager) was used.  We mainly use 2 external dependencies for running this project.

They are
argparse: Argparse is mainly used to parse command line arguments. You can install argparse by typing 
                         
                                      pip install argparse

pass ingredients as command line arguments for running this project. Any ‘N’ number of ingredients can be passed as command line arguments.
You should enter the ingredients as command line arguments in the following fashion.
 
                              python mainprogram.py – ingredients bananas apples

Enter your ingredients after the –ingredients with each ingredient followed by a space.

If you have to enter 3 ingredients, you can use

                             python mainprogram.py –ingredients bananas apples peaches

 The same format can be extended for ‘N’ ingredients.
 
 requests: This package is mainly used to interact with external APIs and get responses.
 You can install requests by typing
                        
                                      pip install requests     

This API takes various parameters like the API Endpoint which we are trying to access and the payload which is nothing but the various parameters which we want to pass to 
 GET API and timeout. For hitting the Spoonacular API, we use the following endpoint

                             https://api.spoonacular.com/recipes/findByIngredients

This Endpoint is used to give recipes which contain the ingredients inputted by the user along with certain additional ingredients required to prepare the recipe. The payload which contains the params for this API has the following parameters

- Ingredients: This is basically the ingredients inputted by the user formatted into a string with each ingredient separated by a comma. The ingredients from the command line are stored as a list and are then converted into a string in the  process_ingredients method in the Ingredients.py file  in the Ingredients package. 

- api_secret_key: The api_secret_key is the secret passphrase which should be passed as a parameter to the GET request to access the API. For safety reasons, this key is stored in the config.py file under the Main package and then imported into the APIService.py file. You should enter your own API key from the Spoonacular website in the config.py file to access the API.

- number:  This is a field used to limit the number of recipes in the API response. I am configuring it to 20. I am not trying to hit the API every time again and again to avoid making
a lot of API calls. This number as of now can be only changed in the code and cannot be changed dynamically because only one recipe is shown to the user for every choice he makes.
 
We hit the API in the APIService.py file in the call_spoonacular_api method and all the errors are validated in the call_api method. The call_api method checks for various errors
which are possible when we hit the Spoonacular API. 

The next step after we get the response_data after hitting the API is to separate the various attributes from the response_data. All the recipes from the API response are stored in a list
which will be available for user selection later on.All the missing ingredients of a recipe are stored in a dictionary with the recipe as the key and the missing ingredients of that recipe stored as a list which is the value for the key. 
All the aisles of the missing ingredients are stored in a dictionary and, similarly all the prices for all the missing ingredients are stored in a dictionary.All of these operations are performed in the process_recipes method.

After this, the recipes are made available for the user to select them. Initially the first recipe, in the recipes list is displayed to the user. If the user chooses to “like” the recipe, all the missing items of the recipe are added to a list.
Similarly, all the aisles of the missing items of the recipes which the user likes are stored in a dictionary.All the prices of the missing items are stored in a dictionary. 

If the item is absent, the price is added for the first time, if the missing item is already present, the price is added to the existing price. Throughout the process, the User is given the option to continue shopping or not to continue shopping.
If the user does not like a recipe,He is presented with a new recipe.If he likes the recipe, he can choose to end shopping. If all the recipes are viewed by the user, we exit out with this message “We have run out of recipes”.

Finally all the missing_ingredients, their corresponding aisles and the prices are displayed to the user in the process_output_to_user method in OutputRecipes.
