from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb+srv://reemakharvi98_db_user:Flask9134@cluster0.xjvsi8n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["studentdb"]
collection = db["students"]


# Task 1 API Route
@app.route('/api')
def api():

    with open('data.json', 'r') as file:
        data = json.load(file)

    return jsonify(data)


# Form Page
@app.route('/')
def home():
    return render_template('form.html')


# Form Submission
@app.route('/submit', methods=['POST'])
def submit():

    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('form.html', error=str(e))


# Success Page
@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)