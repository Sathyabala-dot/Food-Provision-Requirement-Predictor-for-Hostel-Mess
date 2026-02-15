import os
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from build_dataset import build_dataset

# PATH SETUP
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

HOSTEL_ENCODER_PATH = os.path.join(DATA_DIR, "hostel_encoder.pkl")
INGREDIENT_ENCODER_PATH = os.path.join(DATA_DIR, "ingredient_encoder.pkl")
MODEL_PATH = os.path.join(DATA_DIR, "model.pkl")

# LOAD DATA FROM DATABASE
print("🔄 Fetching data from MySQL...")
data = build_dataset()

print("✅ Data loaded successfully!")
print(data.head())
# ENCODING
hostel_enc = LabelEncoder()
ingredient_enc = LabelEncoder()

data["Hostel_Encoded"] = hostel_enc.fit_transform(data["Hostel"])
data["Ingredient_Encoded"] = ingredient_enc.fit_transform(data["Ingredient_Name"])

# FEATURES & TARGET
X = data[["Hostel_Encoded", "Ingredient_Encoded", "Students_Present"]]
y = data["Per_Student_Qty"]

# TRAIN MODEL
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# SAVE MODEL & ENCODERS
joblib.dump(hostel_enc, HOSTEL_ENCODER_PATH)
joblib.dump(ingredient_enc, INGREDIENT_ENCODER_PATH)
joblib.dump(model, MODEL_PATH)

print("\n✅ Model training complete!")
