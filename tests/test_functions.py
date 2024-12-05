from ingredient_detection import detect_ingredients
from recipe_suggestion_engine import suggest_recipes

# Test ingredient detection
scenario = "Lunch Items"
ingredients = detect_ingredients(scenario)
print(f"Detected Ingredients for {scenario}:", ingredients)

# Test recipe suggestions
recipes = suggest_recipes(ingredients)
print("Suggested Recipes:")
for recipe in recipes:
    print(f"- {recipe['name']}")
    if 'missing_ingredients' in recipe:
        print(f"  Missing ingredients: {', '.join(recipe['missing_ingredients'])}")
    else:
        print("  All ingredients available!")
