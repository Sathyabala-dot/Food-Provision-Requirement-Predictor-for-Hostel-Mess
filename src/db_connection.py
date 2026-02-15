import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Murugan@06",
            database="food_prediction"
        )
        return conn
    except mysql.connector.Error as err:
        print("❌ Error connecting to MySQL:", err)
        return None
