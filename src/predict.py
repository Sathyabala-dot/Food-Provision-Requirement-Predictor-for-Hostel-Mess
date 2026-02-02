import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

try:
    model = joblib.load(os.path.join(DATA_DIR, "model.pkl"))
    hostel_enc = joblib.load(os.path.join(DATA_DIR, "hostel_encoder.pkl"))
    ingredient_enc = joblib.load(os.path.join(DATA_DIR, "ingredient_encoder.pkl"))
except Exception as e:
    print("Error loading files:", e)
    exit()

print("\n--- Provision Prediction System ---\n")

date = input("Enter date (YYYY-MM-DD): ").strip()
hostel = input("Enter Hostel (e.g., H1, H2, H3): ").strip()
students_present = int(input("Enter number of students present: ").strip())

# Check hostel validity
if hostel not in hostel_enc.classes_:
    print("\n Hostel not found in training data.")
    print("Available hostels:", list(hostel_enc.classes_))
    exit()

hostel_encoded = hostel_enc.transform([hostel])[0]

print("\nPrediction Results")
print("----------------------")

for ingredient in ingredient_enc.classes_:
    ingredient_encoded = ingredient_enc.transform([ingredient])[0]

    X_input = pd.DataFrame([{
        "Hostel_Encoded": hostel_encoded,
        "Ingredient_Encoded": ingredient_encoded,
        "Students_Present": students_present
    }])

    per_student_qty = model.predict(X_input)[0]
    total_qty = per_student_qty * students_present

    print(f"{ingredient:12s} → {round(per_student_qty, 4)} kg per student | Total: {round(total_qty, 2)} kg")

    
