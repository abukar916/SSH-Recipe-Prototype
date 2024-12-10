import tkinter as tk
from tkinter import messagebox
from ingredient_detection import detect_ingredients
from recipe_suggestion_engine import suggest_recipes

def show_recipes():
   
    # Get the selected scenario from the dropdown menu
    scenario_choice = scenario_var.get()
    if not scenario_choice:
        messagebox.showwarning("Input Error", "Please select a fridge scenario.")
        return

    # Detect ingredients based on the selected scenario
    ingredients = detect_ingredients(scenario_choice)

    # Handle Default and Empty Fridge scenarios
    if scenario_choice == 'Default':
        result_text = "Detected Ingredients:\nwater, juice\n\nNo recipes for this scenario."
    elif scenario_choice == 'Empty Fridge':
        result_text = "Detected Ingredients:\n\nThe fridge is empty. No recipes available."
    else:
        # Get recipe suggestions based on detected ingredients and the scenario
        recipes = suggest_recipes(ingredients, scenario_choice)

        # Build the result text to display
        result_text = f"Detected Ingredients:\n{', '.join(ingredients)}\n\n"
        if not recipes:
            result_text += "No recipes found with the available ingredients."
        else:
            result_text += "Suggested Recipes:\n"
            for recipe in recipes:
                result_text += f"- {recipe['name']}\n"
                if 'missing_ingredients' in recipe:
                    result_text += f"  Missing ingredients: {', '.join(recipe['missing_ingredients'])}\n"
                else:
                    result_text += "  All ingredients available!\n"
                result_text += f"  Instructions: {recipe['instructions']}\n"
                result_text += "\n"

    
    result_label.config(state=tk.NORMAL)
    result_label.delete(1.0, tk.END)
    result_label.insert(tk.END, result_text)
    result_label.config(state=tk.DISABLED)

# Create the main application window
root = tk.Tk()
root.title("Recipe Suggestion System")
root.geometry("600x600")  

# Scenario selection label
scenario_label = tk.Label(root, text="Select a fridge scenario:", font=("Helvetica", 14))
scenario_label.pack(pady=10)

# Variable to hold the selected scenario
scenario_var = tk.StringVar(root)
scenario_var.set('Default')  

scenario_options = [
    'Breakfast Items',
    'Vegetarian',
    'Lunch Items',
    'Dessert Ingredients',
    'Default',
    'Empty Fridge'
]

# Create the dropdown menu for scenario selection
scenario_menu = tk.OptionMenu(root, scenario_var, *scenario_options)
scenario_menu.pack(pady=5)

# Create a button to detect ingredients and suggest recipes
detect_button = tk.Button(root, text="Detect Ingredients", font=("Helvetica", 12), command=show_recipes)
detect_button.pack(pady=20)

# Create a Text widget with a scrollbar for the results
result_frame = tk.Frame(root)
result_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

result_scrollbar = tk.Scrollbar(result_frame)
result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_label = tk.Text(result_frame, height=20, wrap="word", yscrollcommand=result_scrollbar.set, font=("Helvetica", 12))
result_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

result_scrollbar.config(command=result_label.yview)


result_label.config(state=tk.DISABLED)

def run_gui():
    
    root.mainloop()
