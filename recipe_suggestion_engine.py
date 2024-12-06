from recipe_database import get_recipes

def suggest_recipes(available_ingredients, scenario_name):
    """
    Suggests recipes based on available ingredients and the selected scenario.

    Args:
        available_ingredients (list): A list of available ingredients.
        scenario_name (str): The name of the selected fridge scenario.

    Returns:
        list: A list of suggested recipes relevant to the scenario.
    """
    recipes = get_recipes()

    # Handle empty recipe database
    if not recipes:
        print("No recipes available in the database.")
        return []

    suggested_recipes = []

    for recipe in recipes:
        # Scenario filtering
        if scenario_name == 'Breakfast Items' and recipe['cuisine'] != 'Breakfast':
            continue
        if scenario_name == 'Vegetarian' and recipe['cuisine'] != 'Vegetarian':
            continue
        if scenario_name == 'Lunch Items' and recipe['cuisine'] not in ['Libyan', 'Somali', 'Egyptian']:
            continue
        if scenario_name == 'Dessert Ingredients' and recipe['cuisine'] != 'Dessert':
            continue

        # Match ingredients
        required_ingredients = recipe['ingredients']
        missing_ingredients = [item for item in required_ingredients if item not in available_ingredients]

        # Debugging output for ingredient matching
        print(f"Checking Recipe: {recipe['name']}")
        print(f"Required Ingredients: {required_ingredients}")
        print(f"Available Ingredients: {available_ingredients}")
        print(f"Missing Ingredients: {missing_ingredients}")

        if not missing_ingredients:
            # Full match
            suggested_recipes.append(recipe)
        else:
            # Partial match with missing ingredients
            recipe_with_missing = recipe.copy()
            recipe_with_missing['missing_ingredients'] = missing_ingredients
            suggested_recipes.append(recipe_with_missing)

    # Debugging output for suggested recipes
    print(f"Suggested Recipes for Scenario '{scenario_name}': {[recipe['name'] for recipe in suggested_recipes]}")

    return suggested_recipes
