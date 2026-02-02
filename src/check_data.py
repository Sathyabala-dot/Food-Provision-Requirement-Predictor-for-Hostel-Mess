import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

ingredients = pd.read_csv(DATA_DIR / "ingredients_issued.csv")
attendance = pd.read_csv(DATA_DIR / "attendance.csv")
future = pd.read_csv(DATA_DIR / "future_absentees.csv")

print("\n--- Ingredients Issued ---")
print(ingredients.head())

print("\n--- Attendance ---")
print(attendance.head())

print("\n--- Future Absentees ---")
print(future.head())
