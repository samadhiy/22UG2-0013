from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="rootpassword",
            database="testdb"
        )
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS visits (id INT AUTO_INCREMENT PRIMARY KEY, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        cursor.execute("INSERT INTO visits () VALUES ()")
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM visits")
        count = cursor.fetchone()[0]
        return f"<h1>Hello from Flask!</h1><p>Visits so far: {count}</p>"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
