import tomli

def run(): 
    recipes = get_recipes()
    print(recipes)
    choose_recipe("breakfast", recipes)


def get_recipes(): 
    with open("recipes.toml", "rb") as f:
        return tomli.load(f)


def choose_recipe(meal_type, recipes): 
    pass

if __name__ == "__main__": 
    run()
