
# 📄 KPA Backend API Project

## ✅ Project Description
This project implements simple POST and GET APIs using FastAPI and MySQL to store and retrieve form data (name and phone number).

## ✅ Technology Stack
- Python 3.11
- FastAPI
- MySQL Workbench
- mysql-connector-python
- Postman for API testing
- dotenv for environment variables

## ✅ How to Setup and Run Project

### 1. Clone or Download the Project
```bash
git clone <your-repo-link>
cd kpa_backend
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```
Activate it:
- Windows:
```bash
venv\Scripts\activate
```
- Mac/Linux:
```bash
source venv/bin/activate
```

### 3. Install Required Libraries
```bash
pip install -r requirements.txt
```

### 4. Setup MySQL Database
Create database and table in MySQL Workbench:
```sql
CREATE DATABASE kpa_backend;
USE kpa_backend;
CREATE TABLE form_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(20)
);
```

### 5. Setup `.env` file
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_DATABASE=kpa_backend
```

### 6. Run FastAPI Server
```bash
uvicorn main:app --reload
```
Visit: http://127.0.0.1:8000

## ✅ API Endpoints

### 1. POST /form_data
- Method: POST
- Example: http://127.0.0.1:8000/form_data?name=Guru&phone=9876543210

### 2. GET /form_data
- Method: GET
- Example: http://127.0.0.1:8000/form_data

## ✅ Testing
Test the APIs using Postman. A Postman collection file is included.

## ✅ Author
## Your name
Guru

