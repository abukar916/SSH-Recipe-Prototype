def detect_ingredients(scenario_name):
    """
    Simulates ingredient detection based on the fridge scenario.

    Args:
        scenario_name (str): The name of the selected fridge scenario.

    Returns:
        list: A list of detected ingredients.
    """
    fridge_scenarios = {
        'Breakfast Items': ['tomato', 'pepper', 'onion', 'salt', 'eggs', 'toast', 'tuna', 'cheese', 'olive oil'],
        'Vegetarian': ['lettuce', 'cucumber', 'tomato', 'cheese', 'olive', 'spinach', 'vegetables', 'tofu'],
        'Lunch Items': [
            'meat', 'flour', 'potato', 'tomato sauce', 'eggs', 'pepper', 
            'sweet pepper', 'grape leaves', 'spiced rice', 'lamb', 'spices', 
            'onions', 'garlic', 'tomatoes', 'peppers'
        ],
        'Dessert Ingredients': ['milk', 'sugar', 'flour', 'chocolate chips', 'honey', 'lotus', 'cream cheese', 'butter', 'eggs'],
        'Default': ['water', 'juice'],  # Only water and juice
        'Empty Fridge': []  # Empty fridge
    }

    return fridge_scenarios.get(scenario_name, [])
