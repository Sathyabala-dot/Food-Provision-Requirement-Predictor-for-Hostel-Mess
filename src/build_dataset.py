import pandas as pd
from db_connection import get_connection

def build_dataset():

    conn = get_connection()

    # Fetch data from DB
    attendance = pd.read_sql("SELECT * FROM attendance", conn)
    ingredients = pd.read_sql("SELECT * FROM ingredients_issued", conn)
    future = pd.read_sql("SELECT * FROM future_absentees", conn)

    conn.close()

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
    merged["Per_Student_Qty"] = (
        merged["Quantity_Issued"] / merged["Students_Present"]
    )

    return merged


# Test block
if __name__ == "__main__":
    df = build_dataset()
    print("\n✅ Dataset built from DB successfully!\n")
    print(df.head())
