import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Murugan@06",
    database="food_prediction"
)

cursor = conn.cursor()

# -------------------------
# 1️⃣ LOAD ATTENDANCE
# -------------------------
attendance_df = pd.read_csv("data/attendance.csv")
attendance_df["Date"] = pd.to_datetime(attendance_df["Date"]).dt.date

for _, row in attendance_df.iterrows():
    cursor.execute("""
        INSERT INTO attendance 
        (Date, Hostel, Total_Students, Students_Present, Students_Absent)
        VALUES (%s, %s, %s, %s, %s)
    """, tuple(row))

print(f"{len(attendance_df)} attendance rows inserted")


# -------------------------
# 2️⃣ LOAD FUTURE ABSENTEES
# -------------------------
future_df = pd.read_csv("data/future_absentees.csv")
future_df["Date"] = pd.to_datetime(future_df["Date"]).dt.date

for _, row in future_df.iterrows():
    cursor.execute("""
        INSERT INTO future_absentees 
        (Date, Hostel, Expected_Absentees,Reason)
        VALUES (%s, %s, %s,%s)
    """, tuple(row))

print(f"{len(future_df)} future absentees rows inserted")


# -------------------------
# 3️⃣ LOAD INGREDIENTS ISSUED
# -------------------------
ingredients_df = pd.read_csv("data/ingredients_issued.csv")
ingredients_df["Date"] = pd.to_datetime(ingredients_df["Date"]).dt.date

for _, row in ingredients_df.iterrows():
    cursor.execute("""
        INSERT INTO ingredients_issued 
        (Date, Hostel,Caterer_ID, Ingredient_Name,Ingredient_Category, Quantity_Issued, Unit)
        VALUES (%s, %s, %s, %s, %s,%s,%s)
    """, tuple(row))

print(f"{len(ingredients_df)} ingredients rows inserted")


conn.commit()
conn.close()

print("All data inserted successfully!")
