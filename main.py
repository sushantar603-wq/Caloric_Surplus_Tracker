import json
import os
from datetime import datetime

# --- Configuration ---
DATA_FILE = 'diet_data.json'
DAILY_CALORIC_TARGET = 2800  # Target for a caloric surplus

# --- Core Functions ---
def load_data():
    """Loads existing diet data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

def save_data(data):
    """Saves the updated diet data to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def log_meal(data):
    """Prompts the user to log a new meal for today."""
    today = datetime.now().strftime("%Y-%m-%d")
    if today not in data:
        data[today] = []

    print("\n--- Log a Meal ---")
    food_name = input("Enter food name: ").strip()
    
    while True:
        try:
            calories = int(input("Enter calories: "))
            protein = int(input("Enter protein (in grams): "))
            break
        except ValueError:
            print("Please enter valid numbers for calories and protein.")

    meal = {
        "food": food_name,
        "calories": calories,
        "protein": protein,
        "time": datetime.now().strftime("%H:%M:%S")
    }
    
    data[today].append(meal)
    save_data(data)
    print(f"✅ Successfully logged: {food_name} ({calories} kcal)")

def view_daily_summary(data):
    """Displays the total calories and protein for the day vs. the goal."""
    today = datetime.now().strftime("%Y-%m-%d")
    
    print(f"\n--- Summary for {today} ---")
    if today not in data or len(data[today]) == 0:
        print("No meals logged yet today.")
        return

    total_calories = 0
    total_protein = 0

    for meal in data[today]:
        print(f"- {meal['food']} | {meal['calories']} kcal | {meal['protein']}g protein")
        total_calories += meal['calories']
        total_protein += meal['protein']

    print("-" * 25)
    print(f"Total Calories: {total_calories} / {DAILY_CALORIC_TARGET} kcal")
    print(f"Total Protein:  {total_protein}g")
    
    remaining = DAILY_CALORIC_TARGET - total_calories
    if remaining > 0:
        print(f"⚠️ You need {remaining} more calories to hit your surplus goal.")
    else:
        print("🎯 Goal reached! Excellent work on the surplus today.")

# --- Main Application Loop ---
def main():
    print("Welcome to the Caloric Surplus Tracker!")
    data = load_data()

    while True:
        print("\nMain Menu:")
        print("1. Log a new meal")
        print("2. View today's summary")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            log_meal(data)
        elif choice == '2':
            view_daily_summary(data)
        elif choice == '3':
            print("Exiting tracker. Stay consistent!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()