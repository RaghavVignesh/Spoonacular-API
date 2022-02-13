
# Spoonacular API - Readme

This is a project developed in Python 3.9.6 which fetches 
recipes from the Spoonacular API and displays it to the user.

We use 2 pip dependencies to run this project. They are

 - Argparse for parsing command line arguments
 - Requests for interacting with the Spoonacular API

You can run the project by cloning it and running the 
mainprogram.py file and you can pass the ingredients as 
command line arguments

For example: To Run the program with apples and bananas as ingredients, Type

 python mainprogram.py --ingredients apples bananas

You can give any number of ingredients in the following format with each ingredient separated by spaces

When entering "Yes" or "No" when asked to like the recipe. Do not leave spaces. This is important.You need to enter either "Yes" or "No" without spaces from the command prompt message.

For Security Reasons, The secret key for accessing the API is read
from a config file. You will need to enter your own secret key in the config file
for accessing the Spoonacular API for which you need
a Spoonacular Account. 

To avoid, making multiple requests to the API, The API
response has been configured to return 20 recipes for a single
API call. This number can be changed by modifying payload in
APIService.py. I am not giving the option to modify it dynamically
as the user needs to be shown only one recipe at a time.


There are Unit Tests which can be executed by typing
python test_cases.py.

Also make sure you read the technical documentation and user documentation to understand more about the project.




