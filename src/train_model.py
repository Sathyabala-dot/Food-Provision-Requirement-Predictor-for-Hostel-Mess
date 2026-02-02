import os
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

# ========== PATH SETUP ==========
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # src/
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

DATA_PATH = os.path.join(DATA_DIR, "hostel_data.csv")
HOSTEL_ENCODER_PATH = os.path.join(DATA_DIR, "hostel_encoder.pkl")
INGREDIENT_ENCODER_PATH = os.path.join(DATA_DIR, "ingredient_encoder.pkl")
MODEL_PATH = os.path.join(DATA_DIR, "model.pkl")

# ========== LOAD DATA ==========
print("Loading data from:", DATA_PATH)
data = pd.read_csv(DATA_PATH)

# ========== ENCODING ==========
hostel_enc = LabelEncoder()
ingredient_enc = LabelEncoder()

data["Hostel_Encoded"] = hostel_enc.fit_transform(data["Hostel"])
data["Ingredient_Encoded"] = ingredient_enc.fit_transform(data["Ingredient_Name"])

# ========== FEATURES & TARGET ==========
X = data[["Hostel_Encoded", "Ingredient_Encoded", "Students_Present"]]
y = data["Per_Student_Qty"]

# ========== TRAIN MODEL ==========
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# ========== SAVE MODEL & ENCODERS ==========
joblib.dump(hostel_enc, HOSTEL_ENCODER_PATH)
joblib.dump(ingredient_enc, INGREDIENT_ENCODER_PATH)
joblib.dump(model, MODEL_PATH)

print("\n✅ Model training complete!")
print("✅ Files saved:")
print(" -", HOSTEL_ENCODER_PATH)
print(" -", INGREDIENT_ENCODER_PATH)
print(" -", MODEL_PATH)
