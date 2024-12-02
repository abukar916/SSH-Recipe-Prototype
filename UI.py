

import tkinter as tk
from ingredient_detection import detect_ingredients
from recipe_suggestion_engine import suggest_recipes

def show_recipes():
    """
    This function is called when the "Detect Ingredients" button is clicked.
    It simulates ingredient detection, gets recipe suggestions, and updates the GUI.
    """
    # Simulate ingredient detection
    ingredients = detect_ingredients()
    
    # Get recipe suggestions based on detected ingredients
    recipes = suggest_recipes(ingredients)
    
    # Build the result text to display
    if not recipes:
        result_text = "No recipes found with the available ingredients."
    else:
        result_text = f"Detected Ingredients: {', '.join(ingredients)}\n\nSuggested Recipes:\n"
        for recipe in recipes:
            result_text += f"- {recipe['name']}\n"
            # Check for missing ingredients
            if 'missing_ingredients' in recipe and recipe['missing_ingredients']:
                result_text += f"  Missing ingredients: {', '.join(recipe['missing_ingredients'])}\n"
    
    # Update the label with the results
    result_label.config(text=result_text)

# Create the main application window
root = tk.Tk()
root.title("Recipe Suggestion System")

# Optional: Set the window size
root.geometry("400x400")

# Create a button to detect ingredients and suggest recipes
detect_button = tk.Button(root, text="Detect Ingredients", command=show_recipes)
detect_button.pack(pady=10)

# Create a label to display the detected ingredients and suggested recipes
result_label = tk.Label(root, text="", justify="left", wraplength=380)
result_label.pack(padx=10, pady=10)

def run_gui():
    """
    Starts the Tkinter event loop.
    """
    root.mainloop()
