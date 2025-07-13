# Create the README.md content
readme_content = """
# Flask User Input App with MySQL and Server IP Display

A simple Flask web application that accepts user information (name and email), stores it in a MySQL database (such as Amazon RDS), and displays the server's IP address on the homepage.

---

## 🚀 Features

- 📥 User input form (name & email)
- 🛢 Stores data in MySQL database
- 🌐 Displays server IP address
- 📋 View all user entries

---

## 🛠 Requirements

- Python 3.x
- Flask
- PyMySQL
- A MySQL-compatible database (e.g., Amazon RDS)

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-user-input-app.git
   cd flask-user-input-app
   ```
2. Install dependencies
```   
   bash
   Copy
   Edit
   pip install Flask PyMySQL
```
3. Configure your database
Edit the database settings in app.py:
```
   python
   Copy
   Edit
   DB_HOST = 'your-rds-endpoint'
   DB_USER = 'your-db-username'
   DB_PASSWORD = 'your-db-password'
   DB_NAME = 'db_lab'
```
4. Run the application
```
python app.py
```
---

## Project Structure 

```
.
├── app.py
├── templates/
│   ├── index.html
│   ├── success.html
│   └── view_data.html
├── static/
│   └── css/
│       └── styles.css
```
