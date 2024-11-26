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


## Prototype Summary
Our team chose the Engineering Design Review by Anas Khurmani on the Recipe Suggestion System Using Fridge Data for prototype implementation. This system is supposed to enhance meal planning and reduce food wastage by the use of smart home technology. It makes use of an SSH camera that detects the contents of a fridge, then processes those through the SSH Cloud, matching them up with recipes kept in a cloud-based database. It then makes personalized recipe suggestions via a mobile app interface.

Key Features:
- Detection of the ingredients and matching for recipes.
- Recommendations based on user preferences and available ingredients.
- Notifications about missing ingredients and efficient grocery planning.

This prototype focuses on the emulation of core functionalities: detecting the fridge content, proposing recipes, and managing missing ingredients by interaction with the user. In the implementation, Python was used to mock data capture and a database of recipes to maintain the demo simplicity while functional. The system is completely automated for convenience, with least mechanical input.

We mitigated the limited scope of the prototype by substituting simulated data for actual camera inputs and by integrating static recipes instead of dynamic API integrations. This approach ensures that the viability of the design in respect to the constraints of the project is maintained.

This includes a recipe suggestion engine that works, modular code, and comprehensive tests to set a strong foundation for any further development.


