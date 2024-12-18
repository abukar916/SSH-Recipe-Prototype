import unittest
from unittest.mock import patch
from recipe_suggestion_engine import suggest_recipes
from recipe_database import get_recipes
from ingredient_detection import detect_ingredients

class TestRecipeSuggestionSystem(unittest.TestCase):

    def setUp(self):
        
        self.recipes = get_recipes()

    def test_ingredient_detection(self):
       
        scenario = "Lunch Items"
        expected_ingredients = [
            'meat', 'flour', 'potato', 'tomato sauce', 'eggs', 'pepper', 
            'sweet pepper', 'grape leaves', 'spiced rice', 'lamb', 'spices', 
            'onions', 'garlic', 'tomatoes', 'peppers'
        ]

        detected_ingredients = detect_ingredients(scenario)
        self.assertListEqual(detected_ingredients, expected_ingredients)

    def test_full_match(self):
       
        # Prepare test data
        ingredients = ['toast', 'tuna', 'cheese', 'olive oil']
        scenario_name = "Breakfast Items"

        # Call the function
        suggested_recipes = suggest_recipes(ingredients, scenario_name)

        # Extract recipe names where there are no missing ingredients
        full_match_recipes = [
            recipe['name'] for recipe in suggested_recipes
            if 'missing_ingredients' not in recipe or not recipe['missing_ingredients']
        ]

        # Assertions
        expected_recipes = ['Cheese Tuna Toast']
        self.assertCountEqual(full_match_recipes, expected_recipes)

    def test_partial_match(self):
        
        ingredients = ['eggs', 'milk']
        scenario_name = "Breakfast Items"

        suggested_recipes = suggest_recipes(ingredients, scenario_name)
        recipe = next((r for r in suggested_recipes if r['name'] == 'Shakshuka'), None)

        self.assertIsNotNone(recipe, "Recipe should be suggested even with missing ingredients.")
        self.assertIn('missing_ingredients', recipe)
        self.assertEqual(recipe['missing_ingredients'], ['tomato', 'pepper', 'onion', 'salt'])

    def test_no_ingredients(self):
      
        ingredients = []
        scenario_name = "Breakfast Items"

        suggested_recipes = suggest_recipes(ingredients, scenario_name)

        for recipe in suggested_recipes:
            self.assertEqual(set(recipe['ingredients']), set(recipe.get('missing_ingredients', [])))

    def test_no_recipes_available(self):
        
        ingredients = ['eggs', 'milk']
        with patch('recipe_suggestion_engine.get_recipes', return_value=[]):
            suggested_recipes = suggest_recipes(ingredients, "Breakfast Items")
        self.assertEqual(len(suggested_recipes), 0)

if __name__ == "_main_":
    unittest.main()
