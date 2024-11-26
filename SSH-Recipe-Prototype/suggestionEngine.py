import random

# Simulating SSH Camera data capture for fridge items
def get_fridge_contents():
    return {
        "milk": random.randint(0, 2),
        "eggs": random.randint(0, 12),
        "butter": random.randint(0, 1),
        "cheese": random.randint(0, 3),
        "spinach": random.randint(0, 1),
        "tomato": random.randint(0, 2),
        "bread": random.randint(0, 4),
    }

# Simulating a recipe database
recipe_database = [
    {
        "name": "Cheese Omelette",
        "ingredients": ["eggs", "cheese", "butter"],
        "cooking_time": 10,
        "dietary_preference": "vegetarian",
    },
    {
        "name": "Spinach Salad",
        "ingredients": ["spinach", "cheese"],
        "cooking_time": 5,
        "dietary_preference": "vegetarian",
    },
    {
        "name": "French Toast",
        "ingredients": ["milk", "eggs", "butter", "bread"],
        "cooking_time": 15,
        "dietary_preference": "vegetarian",
    },
    {
        "name": "Tomato Sandwich",
        "ingredients": ["tomato", "bread", "butter"],
        "cooking_time": 5,
        "dietary_preference": "vegetarian",
    },
]

# Recipe Suggestion Engine
def suggest_recipes(fridge_contents, user_preferences=None):
    suggested_recipes = []
    for recipe in recipe_database:
        # Check if all ingredients are available in the fridge
        available = True
        for ingredient in recipe["ingredients"]:
            if fridge_contents.get(ingredient, 0) == 0:
                available = False
                break
        if available:
            # Check dietary preference if any
            if user_preferences and recipe["dietary_preference"] != user_preferences:
                continue
            suggested_recipes.append(recipe)
    return suggested_recipes

# Mock function for user preferences
def get_user_preferences():
    return "vegetarian"  # Hardcoded for prototype

# Function to add missing ingredients
def add_missing_ingredients(missing_ingredients):
    print("\nThe following ingredients are missing:")
    for ingredient in missing_ingredients:
        print(f"- {ingredient}")
    print("\nAdding missing ingredients to fridge...")
    return {ingredient: 1 for ingredient in missing_ingredients}

# Enhanced Recipe Suggestion with Missing Ingredients Handling
def suggest_recipes_with_missing(fridge_contents, user_preferences=None):
    suggested_recipes = []
    missing_ingredients = []
    for recipe in recipe_database:
        available = True
        for ingredient in recipe["ingredients"]:
            if fridge_contents.get(ingredient, 0) == 0:
                available = False
                missing_ingredients.append(ingredient)
        if available:
            if user_preferences and recipe["dietary_preference"] != user_preferences:
                continue
            suggested_recipes.append(recipe)

    if not suggested_recipes and missing_ingredients:
        fridge_contents.update(add_missing_ingredients(missing_ingredients))
        suggested_recipes = suggest_recipes(fridge_contents, user_preferences)
    
    return suggested_recipes

# Main function to simulate interaction
def main():
    # Simulating fridge contents
    fridge_contents = get_fridge_contents()
    print("Current fridge contents:")
    for item, quantity in fridge_contents.items():
        print(f"{item}: {quantity}")

    # Fetch user dietary preferences
    user_preferences = get_user_preferences()
    print("\nUser dietary preferences:")
    print(user_preferences)

    # Suggest recipes
    suggested_recipes = suggest_recipes_with_missing(fridge_contents, user_preferences)
    print("\nSuggested Recipes:")
    if suggested_recipes:
        for recipe in suggested_recipes:
            print(f"- {recipe['name']} (Cooking time: {recipe['cooking_time']} mins)")
    else:
        print("No recipes could be suggested even after adding missing ingredients.")

if __name__ == "__main__":
    main()
