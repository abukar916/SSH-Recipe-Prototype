# SSH-Recipe-Prototype

This repository contains a Python-based prototype for a smart recipe suggestion system that integrates with a simulated smart fridge environment. The project aims to minimize food waste and simplify meal planning by leveraging simulated fridge data and suggesting recipes tailored to available ingredients and meal preferences.

![SSH-Recipe-Prototype CI](https://github.com/abukar916/SSH-Recipe-Prototype/workflows/SSH-Recipe-Prototype%20CI/badge.svg)
***This status badge was added to show the Continous Integration status.***

## Features
- **Ingredient Detection**: Simulates a smart fridge's camera capturing ingredient data based on user-selected scenarios.
- **Recipe Suggestion Engine**: Suggests recipes based on the currently available ingredients, meal type preferences, and dietary options.
- **Handling Missing Ingredients**: Highlights which ingredients are missing for a given recipe and allows for simulating their addition, ensuring the user can still proceed with meal preparation.

## How It Works
1. **Fridge Content Simulation**: Instead of a real camera, the fridge contents are selected by a user-chosen scenario (e.g., "Breakfast Items" or "Dessert Ingredients").
2. **Recipe Database**: A predefined set of recipes is included, each with its required ingredients, meal type (breakfast, dessert, etc.), and other optional metadata like dietary preferences.
3. **Recipe Suggestion**: The suggestion engine compares the available fridge ingredients against the recipe database to find suitable matches. Missing ingredients are identified and listed for the user
4. **Graphical User Interface (GUI)**: A Tkinter-based GUI lets users select a scenario, detect the "ingredients," and view suggested recipes and missing ingredients directly from a simple interface.

## Project Structure
- **main.py**: Entry point of the application. Runs the GUI and orchestrates the interaction between ingredient detection and recipe suggestion.
- **gui.py**: Contains the graphical interface logic using Tkinter. Handles user interactions like scenario selection and displays suggested recipes.
- **ingredient_detection.py**: Simulates ingredient detection based on the chosen scenario and returns a corresponding list of ingredients.
- **recipe_suggestion_engine.py**: Implements the logic for matching available ingredients to recipes, filtering by meal type, and identifying missing ingredients.
- **recipe_database.py**: Provides a predefined list of recipes and their required ingredients.
- **tests**: Contains unit tests that verify the functionality of the recipe suggestion engine, ingredient detection, and other components. Running these tests ensures that recent changes haven’t introduced regressions.

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/abukar916/SSH-Recipe-Prototype.git
   ```
2. Navigate to the project directory:
   ```sh
   cd SSH-Recipe-Prototype
   ```
3. Run the main script:
   ```sh
   python main.py
   ```
4. Using the GUI:
   -Select a fridge scenario from the dropdown menu.
   -Click "Detect Ingredients" to view suggested recipes and missing ingredients.
   
6. Running Tests
   ```sh
   python -m unittest discover tests
    ```

## Continous Integration 
This project uses GitHub Actions for continuous integration.The status badge at the top of this README reflects the current build status.

## Requirements
- Python 3.x
- Tkinter: Typically included with most Python installations. No additional external libraries are required.

## Notes
-Extensibility:
The code is organized to allow easy addition of new recipes, scenarios, or features, should you wish to expand the prototype.

