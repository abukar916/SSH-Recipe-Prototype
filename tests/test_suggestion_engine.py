# tests/test_suggestion_engine.py

import unittest
from recipe_suggestion_engine import suggest_recipes
from recipe_database import get_recipes

class TestSuggestionEngine(unittest.TestCase):

    def setUp(self):
        """
        Set up test fixtures. This method is called before every test case.
        """
        self.recipes = get_recipes()

    def test_full_match(self):
        """
        Test that suggest_recipes returns recipes with no missing ingredients
        when all required ingredients are available.
        """
        # Prepare test data
        ingredients = ['eggs', 'milk', 'cheddar cheese', 'bread', 'butter']
        expected_recipe_names = ['Omelette', 'Grilled Cheese Sandwich', 'Pancakes']

        # Call the function
        suggested_recipes = suggest_recipes(ingredients)

        # Extract recipe names where there are no missing ingredients
        full_match_recipes = [
            recipe['name'] for recipe in suggested_recipes
            if 'missing_ingredients' not in recipe or not recipe['missing_ingredients']
        ]

        # Check that all expected recipes are in the full match list
        for recipe_name in expected_recipe_names:
            self.assertIn(recipe_name, full_match_recipes)

    def test_partial_match(self):
        """
        Test that suggest_recipes returns recipes with missing ingredients
        when some required ingredients are missing.
        """
        # Prepare test data
        ingredients = ['eggs', 'milk']
        expected_recipe_name = 'Omelette'
        expected_missing_ingredients = ['cheddar cheese']

        # Call the function
        suggested_recipes = suggest_recipes(ingredients)

        # Find the specific recipe
        recipe = next((r for r in suggested_recipes if r['name'] == expected_recipe_name), None)

        # Assertions
        self.assertIsNotNone(recipe, "Recipe should be suggested even with missing ingredients.")
        self.assertIn('missing_ingredients', recipe, "Recipe should include missing ingredients.")
        self.assertEqual(recipe['missing_ingredients'], expected_missing_ingredients)

    def test_no_ingredients(self):
        """
        Test that suggest_recipes handles the case when no ingredients are available.
        """
        # Prepare test data
        ingredients = []
        
        # Call the function
        suggested_recipes = suggest_recipes(ingredients)

        # Assertions
        self.assertTrue(len(suggested_recipes) > 0, "Should still return recipes even if no ingredients are available.")

        # Check that all recipes have all ingredients missing
        for recipe in suggested_recipes:
            self.assertEqual(
                set(recipe['ingredients']),
                set(recipe.get('missing_ingredients', [])),
                f"All ingredients for {recipe['name']} should be missing."
            )

    def test_no_recipes_available(self):
        """
        Test that suggest_recipes returns an empty list when there are no recipes in the database.
        """
        # Prepare test data
        ingredients = ['eggs', 'milk', 'cheddar cheese']

        # Empty the recipes list
        original_recipes = self.recipes.copy()
        self.recipes.clear()

        # Call the function
        suggested_recipes = suggest_recipes(ingredients)

        # Restore the recipes
        self.recipes.extend(original_recipes)

        # Assertions
        self.assertEqual(len(suggested_recipes), 0, "Should return an empty list when no recipes are available.")

    def test_all_recipes_available(self):
        """
        Test that suggest_recipes returns all recipes when all ingredients are available.
        """
        # Prepare test data
        # Collect all unique ingredients from all recipes
        all_ingredients = set()
        for recipe in self.recipes:
            all_ingredients.update(recipe['ingredients'])
        ingredients = list(all_ingredients)

        # Call the function
        suggested_recipes = suggest_recipes(ingredients)

        # Assertions
        self.assertEqual(len(suggested_recipes), len(self.recipes), "All recipes should be suggested.")

        # Check that none of the recipes have missing ingredients
        for recipe in suggested_recipes:
            self.assertNotIn('missing_ingredients', recipe, f"{recipe['name']} should not have missing ingredients.")

if __name__ == '__main__':
    unittest.main()
