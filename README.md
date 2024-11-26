# SSH-Recipe-Prototype

This repository contains a Python-based prototype for a smart recipe suggestion system that integrates with a simulated smart fridge. The project leverages data captured from a simulated SSH Camera to suggest personalized recipes, aiming to minimize food wastage and simplify meal planning.

## Features
- **Ingredient Detection**: Simulates a smart fridge capturing ingredient data.
- **Recipe Suggestion Engine**: Suggests recipes based on available fridge ingredients and user preferences.
- **Handling Missing Ingredients**: Automatically adds missing ingredients to ensure users can proceed with recipe suggestions.

## How It Works
1. **Fridge Content Simulation**: Ingredients are randomly generated to simulate real-time fridge data.
2. **Recipe Database**: A predefined set of recipes is stored, each with ingredients, cooking time, and dietary preferences.
3. **Recipe Suggestion**: The engine matches fridge contents to available recipes, taking user preferences into account.
4. **User Interaction**: Missing ingredients are added interactively to ensure all suggested recipes can be made.

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
   python recipe_suggestion.py
   ```

## Requirements
- Python 3.x
- No external libraries are required for this basic prototype.




