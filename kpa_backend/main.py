from fastapi import FastAPI, HTTPException
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("localhost"),
        user=os.getenv("root"),
        password=os.getenv("Gaurav@18"),
        database=os.getenv("kpa_backend")
    )

@app.post("/form_data")
def add_data(name: str, phone: str):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO form_data (name, phone) VALUES (%s, %s)"
    cursor.execute(sql, (name, phone))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Data inserted successfully"}

@app.get("/form_data")
def get_data():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM form_data")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
