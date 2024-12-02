# suggestionEngine.py

from backend.ingredient_detector import detect_ingredients  # Import the ingredient detection function

# Recipe database (hardcoded for now)
recipes = [
    {"name": "Pasta", "ingredients": {"Tomato": 2, "Cheese": 1}, "cooking_time": 30},
    {"name": "Salad", "ingredients": {"Lettuce": 1, "Tomato": 1}, "cooking_time": 15}
]

# Recipe matching logic
def match_ingredients(fridge_ingredients, recipe):
    """
    Matches ingredients in the fridge with the recipe ingredients.

    Args:
        fridge_ingredients (dict): Ingredients available in the fridge.
        recipe (dict): Recipe to match with fridge ingredients.

    Returns:
        bool: True if all ingredients are available in the fridge, False otherwise.
    """
    for ingredient, quantity in recipe['ingredients'].items():
        # Check if each ingredient is available and has enough quantity
        if ingredient not in fridge_ingredients or fridge_ingredients[ingredient] < quantity:
            return False
    return True

# Main function to match recipes with fridge ingredients
def main():
    """
    Main function to run the recipe suggestion logic.
    """
    # Simulate ingredient detection (use a test image path)
    detected_ingredients = detect_ingredients('path_to_image.jpg')  # Replace with actual image path
    
    # Create a dictionary of detected ingredients and their counts
    fridge_ingredients = {ingredient: detected_ingredients.count(ingredient) for ingredient in detected_ingredients}
    
    # Check if any recipes can be made with the available ingredients
    for recipe in recipes:
        if match_ingredients(fridge_ingredients, recipe):
            print(f"Suggested Recipe: {recipe['name']} (Cooking time: {recipe['cooking_time']} mins)")

# Run the main function
if __name__ == "__main__":
    main()

# Initial setup complete - testing pull request
print("Hello from the initial setup branch!")
