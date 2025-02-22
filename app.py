from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Database configuration
DB_HOST = 'your-rds-endpoint'
DB_USER = 'your-db-username'
DB_PASSWORD = 'your-db-password'
DB_NAME = 'db_lab'

# Connect to the database
def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# Create a table if it doesn't exist
def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
    ''')
    connection.commit()
    cursor.close()
    connection.close()

# Home route with form
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Insert data into the database
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('success'))

# Success page
@app.route('/success')
def success():
    return render_template('success.html')

# View all user data
@app.route('/view-data')
def view_data():
    connection = get_db_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('view_data.html', users=users)

if __name__ == '__main__':
    create_table()  # Ensure the table exists
    app.run(host='0.0.0.0', port=5000)
