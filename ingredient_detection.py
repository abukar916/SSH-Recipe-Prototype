def detect_ingredients(scenario_name):
   
    fridge_scenarios = {
        'Breakfast Items': ['tomato', 'pepper', 'onion', 'salt', 'eggs', 'toast', 'tuna', 'cheese', 'olive oil'],
        'Vegetarian': ['lettuce', 'cucumber', 'tomato', 'cheese', 'olive', 'spinach', 'vegetables', 'tofu'],
        'Lunch Items': [
            'meat', 'flour', 'potato', 'tomato sauce', 'eggs', 'pepper', 
            'sweet pepper', 'grape leaves', 'spiced rice', 'lamb', 'spices', 
            'onions', 'garlic', 'tomatoes', 'peppers'
        ],
        'Dessert Ingredients': ['milk', 'sugar', 'flour', 'chocolate chips', 'honey', 'lotus', 'cream cheese', 'butter', 'eggs'],
        'Default': ['water', 'juice'],  
        'Empty Fridge': [] 
    }

    return fridge_scenarios.get(scenario_name, [])
