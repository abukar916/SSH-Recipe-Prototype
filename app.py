from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the SSH Recipe System!"

@app.route('/recipes')
def recipes():
    sample_recipes = [
        {"name": "Tomato Salad", "ingredients": ["tomato", "lettuce"], "steps": "Mix tomato and lettuce."},
        {"name": "Cheese Sandwich", "ingredients": ["cheese", "bread"], "steps": "Layer cheese on bread."}
    ]
    return render_template('recipes.html', recipes=sample_recipes)

if __name__ == '__main__':
    app.run(debug=True)
