import os
import pandas as pd
import joblib
from db_connection import get_connection
from datetime import datetime

# ================= PATH SETUP =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # points to src/
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

MODEL_PATH = os.path.join(DATA_DIR, "model.pkl")
HOSTEL_ENCODER_PATH = os.path.join(DATA_DIR, "hostel_encoder.pkl")
INGREDIENT_ENCODER_PATH = os.path.join(DATA_DIR, "ingredient_encoder.pkl")

# ================= LOAD MODEL & ENCODERS =================
try:
    model = joblib.load(MODEL_PATH)
    hostel_enc = joblib.load(HOSTEL_ENCODER_PATH)
    ingredient_enc = joblib.load(INGREDIENT_ENCODER_PATH)
    print("✅ Model and encoders loaded successfully!\n")
except Exception as e:
    print("❌ Error loading model or encoders:", e)
    exit()


# ================= PREDICTION FUNCTION =================
def predict_for_input(input_date: str, hostel: str, students_present: int = None):
    """
    Predict ingredient quantities for a given date, hostel, and student count.
    If student count is None, it will try to fetch from the database.
    """
    # Validate date format
    try:
        date_obj = datetime.strptime(input_date, "%Y-%m-%d").date()
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")
        return

    # If students_present is None, try fetching from DB
    if students_present is None:
        conn = get_connection()
        if conn is None:
            print("❌ Database connection failed.")
            return

        query = f"""
            SELECT Students_Present
            FROM attendance
            WHERE Date = '{date_obj}' AND Hostel = '{hostel}'
        """
        df = pd.read_sql(query, conn)
        conn.close()

        if df.empty:
            print(f"⚠ No attendance data found for {hostel} on {date_obj}.")
            return

        students_present = df.iloc[0]["Students_Present"]

    # Check if hostel exists in encoder
    if hostel not in hostel_enc.classes_:
        print(f"⚠ Hostel '{hostel}' not found in training data.")
        return

    hostel_encoded = hostel_enc.transform([hostel])[0]

    print(f"\n🔮 Predictions for {hostel} on {date_obj} with {students_present} students")
    print("--------------------------------------------------")

    for ingredient in ingredient_enc.classes_:
        ingredient_encoded = ingredient_enc.transform([ingredient])[0]

        X_input = pd.DataFrame([{
            "Hostel_Encoded": hostel_encoded,
            "Ingredient_Encoded": ingredient_encoded,
            "Students_Present": students_present
        }])

        per_student_qty = model.predict(X_input)[0]
        total_qty = per_student_qty * students_present

        print(
            f"{ingredient:12s} → "
            f"{round(total_qty, 2)} kg "
            f"({round(per_student_qty, 4)} kg per student)"
        )


# ================= RUN =================
if __name__ == "__main__":
    hostel_input = input("Enter Hostel Name: ")
    date_input = input("Enter Date (YYYY-MM-DD): ")
    students_input_raw = input("Enter Number of Students (leave blank to fetch from DB): ")

    students_input = int(students_input_raw) if students_input_raw.strip() else None

    predict_for_input(date_input, hostel_input, students_input)
