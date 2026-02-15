from db_connection import get_connection

conn = get_connection()

if conn and conn.is_connected():
    print("✅ Connected to MySQL successfully!")
    conn.close()
else:
    print("❌ Connection failed.")
