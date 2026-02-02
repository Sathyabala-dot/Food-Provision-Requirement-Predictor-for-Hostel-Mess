import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

attendance = pd.read_csv(os.path.join(DATA_DIR, "attendance.csv"))
ingredients = pd.read_csv(os.path.join(DATA_DIR, "ingredients_issued.csv"))
future = pd.read_csv(os.path.join(DATA_DIR, "future_absentees.csv"))

# Merge ingredients + attendance
merged = pd.merge(
    ingredients,
    attendance,
    on=["Date", "Hostel"],
    how="left"
)

# Merge future absentees
merged = pd.merge(
    merged,
    future,
    on=["Date", "Hostel"],
    how="left"
)

# Compute per-student quantity
merged["Per_Student_Qty"] = merged["Quantity_Issued"] / merged["Students_Present"]

output_path = os.path.join(DATA_DIR, "hostel_data.csv")
merged.to_csv(output_path, index=False)

print("Dataset created:", output_path)
print(merged.head())
