from flask import Flask
import psycopg2

app = Flask(__name__)

# Database Connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="db",
        port="5432"
    )
    return conn

@app.route('/')
def index():
    return """
        <h1>Welcome to My Microservices App</h1>
        <p>Name: Srinath</p>
        <p>Register Number: 2022BCD0015</p>
        <p>Short Bio: Passionate about Machine Learning, AI, and Software Development.</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

