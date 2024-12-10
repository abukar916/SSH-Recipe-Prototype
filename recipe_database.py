def get_recipes():
    recipes = [
        # Breakfast Recipes
        {
            'name': 'Shakshuka',
            'ingredients': ['tomato', 'pepper', 'onion', 'salt', 'eggs'],
            'instructions': 'Cook onion, tomato, pepper, and salt in a pan, then add eggs on top.',
            'cuisine': 'Breakfast',
            'dietary_preferences': ['vegetarian']
        },
        {
            'name': 'Cheese Tuna Toast',
            'ingredients': ['toast', 'tuna', 'cheese', 'olive oil'],
            'instructions': 'Spread tuna on toast, add cheese, drizzle olive oil, and toast it.',
            'cuisine': 'Breakfast',  
            'dietary_preferences': []
        },

        # Vegetarian Recipes
        {
            'name': 'Normal Salad',
            'ingredients': ['lettuce', 'cucumber', 'tomato', 'cheese', 'olive'],
            'instructions': 'Chop all ingredients, mix in a bowl, and serve.',
            'cuisine': 'Vegetarian',
            'dietary_preferences': ['vegetarian']
        },
        {
            'name': 'Vegan Burger',
            'ingredients': ['vegetables', 'tofu', 'spinach'],
            'instructions': 'Grill vegetables and tofu, assemble with spinach in a bun.',
            'cuisine': 'Vegetarian',
            'dietary_preferences': ['vegan']
        },

        # Lunch Recipes
        {
            'name': 'Bazin',
            'ingredients': ['meat', 'flour', 'potato', 'tomato sauce', 'eggs', 'pepper'],
            'instructions': (
                'Cook meat, add tomato sauce, pepper, and spices. '
                'Prepare dough with flour and olive oil, bake, then serve with sauce and eggs.'
            ),
            'cuisine': 'Libyan',
            'dietary_preferences': []
        },
        {
            'name': 'Mahshi',
            'ingredients': ['sweet pepper', 'grape leaves', 'spiced rice'],
            'instructions': 'Stuff sweet pepper and grape leaves with spiced rice, bake until tender.',
            'cuisine': 'Egyptian',
            'dietary_preferences': ['vegetarian']
        },
        {
            'name': 'Haneed',
            'ingredients': ['lamb', 'spices'],
            'instructions': 'Dry-rub lamb with spices, cook in the oven at low temperature for six hours.',
            'cuisine': 'Somali',
            'dietary_preferences': []
        },
        {
            'name': 'Suqaar',
            'ingredients': ['lamb', 'spices', 'onions', 'peppers', 'garlic', 'tomatoes', 'pepper'],
            'instructions': 'Cook lamb with spices, then add onions, peppers, garlic, and tomatoes. Simmer until tender.',
            'cuisine': 'Somali',
            'dietary_preferences': []
        },

        # Dessert Recipes
        {
            'name': 'Molten Cake',
            'ingredients': ['chocolate chips', 'butter', 'sugar', 'flour', 'eggs'],
            'instructions': 'Bake chocolate mixture in ramekins until gooey inside.',
            'cuisine': 'Dessert',
            'dietary_preferences': ['vegetarian']
        },
        {
            'name': 'Cheesecake',
            'ingredients': ['cream cheese', 'sugar', 'flour', 'eggs', 'butter'],
            'instructions': 'Bake crust, mix filling, bake until set.',
            'cuisine': 'Dessert',
            'dietary_preferences': ['vegetarian']
        },
        {
            'name': 'Honey Lotus Cake',
            'ingredients': ['lotus', 'honey', 'flour', 'butter', 'sugar'],
            'instructions': 'Mix lotus and honey into cake batter, bake until golden.',
            'cuisine': 'Dessert',
            'dietary_preferences': ['vegetarian']
        }
    ]
    return recipes
