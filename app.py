from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'habits.json'

def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return []

def save_habits(habits):
    with open(DATA_FILE, 'w') as f:
        json.dump(habits, f)

@app.route('/')
def index():
    habits = load_habits()
    return render_template('index.html', habits=habits)

@app.route('/add', methods=['POST'])
def add_habit():
    habit_name = request.form.get('habit')
    if habit_name:
        habits = load_habits()
        habits.append({"name": habit_name, "done": False})
        save_habits(habits)
    return redirect(url_for('index'))

@app.route('/toggle/<int:habit_id>', methods=['POST'])
def toggle_habit(habit_id):
    habits = load_habits()
    if 0 <= habit_id < len(habits):
        habits[habit_id]['done'] = not habits[habit_id]['done']
        save_habits(habits)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
