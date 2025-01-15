Creating a comprehensive Python program for an AI-driven app like "smart-nutrient" involves several components. To keep this example manageable, I'll provide a simplified version focusing on core features such as tracking nutrients, suggesting meals, and handling basic personalization. This script won't include machine learning aspects due to the complexity but will focus on structuring an app that could be expanded for AI integration.

```python
import json

# Sample data
user_profiles = {
    "user_1": {
        "age": 30,
        "weight": 70,
        "height": 175,
        "dietary_requirements": ["gluten-free"],
        "health_goals": ["weight_loss"]
    }
}

meal_database = [
    {
        "name": "Grilled Chicken Salad",
        "nutrients": {"calories": 300, "protein": 30, "fat": 10, "carbs": 20},
        "dietary_tags": ["gluten-free", "low-carb"],
    },
    {
        "name": "Vegan Quinoa Bowl",
        "nutrients": {"calories": 400, "protein": 15, "fat": 15, "carbs": 55},
        "dietary_tags": ["vegan", "gluten-free"],
    }
]

def calculate_bmi(weight, height):
    """Calculate BMI from weight (kg) and height (cm)"""
    try:
        height_in_meters = height / 100
        bmi = weight / (height_in_meters ** 2)
        return round(bmi, 2)
    except Exception as e:
        print(f"Error calculating BMI: {e}")
        return None

def recommend_meals(user_id):
    """Recommend meals based on user's dietary requirements and health goals"""
    user = user_profiles.get(user_id)
    if not user:
        print("User not found.")
        return []
    
    recommended_meals = []
    for meal in meal_database:
        if all(tag in meal["dietary_tags"] for tag in user["dietary_requirements"]):
            recommended_meals.append(meal)
    
    return recommended_meals

def track_intake(user_id, meal_name):
    """Track nutrient intake based on selected meal"""
    user = user_profiles.get(user_id)
    if not user:
        print("User not found.")
        return {}
    
    meal = next((meal for meal in meal_database if meal["name"] == meal_name), None)
    if not meal:
        print("Meal not found.")
        return {}

    return meal["nutrients"]

def user_dashboard(user_id):
    """User dashboard to display personalized info"""
    user = user_profiles.get(user_id)
    if not user:
        print("User not found.")
        return

    print(f"User: {user_id}")
    print(f"Age: {user['age']}")
    print(f"Weight: {user['weight']} kg")
    print(f"Height: {user['height']} cm")
    bmi = calculate_bmi(user['weight'], user['height'])
    if bmi:
        print(f"BMI: {bmi}")
    
    print("Recommended Meals:")
    meals = recommend_meals(user_id)
    for meal in meals:
        print(f"- {meal['name']} (Calories: {meal['nutrients']['calories']}, Protein: {meal['nutrients']['protein']}g)")
    
if __name__ == "__main__":
    try:
        user_id = "user_1"
        user_dashboard(user_id)

        # Example of tracking meal intake
        meal_choice = "Grilled Chicken Salad"
        nutrients = track_intake(user_id, meal_choice)
        if nutrients:
            print(f"\nTracking meal: {meal_choice}")
            print(f"Nutrient intake from {meal_choice}: {json.dumps(nutrients, indent=2)}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Key Components:

1. **User Profile**: A dictionary for storing user data including age, weight, height, and dietary needs.
2. **Meal Database**: A list of meals with associated nutrients and dietary tags.
3. **Calculate BMI**: Function to compute the Body Mass Index using weight and height.
4. **Meal Recommendations**: Function to suggest meals that match user dietary requirements.
5. **Nutrient Tracking**: Function to record nutritional intake from selected meals.
6. **User Dashboard**: A simple interface for displaying user details and recommended meals.
7. **Error Handling**: Using try-except blocks to catch and handle potential errors gracefully.

This simple framework can be expanded with more sophisticated AI methods, database integration, and richer user data for a fully-fledged smart nutrient app.