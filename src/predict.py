import os
import pandas as pd
import joblib
from db_connection import get_connection
from datetime import date

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
def predict_today():

    conn = get_connection()

    if conn is None:
        print("❌ Database connection failed.")
        return

    today = date.today()

    query = f"""
        SELECT Date, Hostel, Students_Present
        FROM attendance
        WHERE Date = '{today}'
    """

    today_data = pd.read_sql(query, conn)
    conn.close()

    if today_data.empty:
        print(f"⚠ No attendance data found for {today}.")
        return

    print(f"\n🔮 Predictions for {today}")
    print("--------------------------------------------------")

    for _, row in today_data.iterrows():

        hostel = row["Hostel"]
        students_present = row["Students_Present"]

        if hostel not in hostel_enc.classes_:
            print(f"⚠ Hostel '{hostel}' not found in training data.")
            continue

        hostel_encoded = hostel_enc.transform([hostel])[0]

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
                f"{hostel} | {ingredient:12s} → "
                f"{round(total_qty, 2)} kg "
                f"({round(per_student_qty, 4)} kg per student)"
            )


# ================= RUN =================
if __name__ == "__main__":
    predict_today()
