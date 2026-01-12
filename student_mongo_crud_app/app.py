"""
app.py
Multi-file Flask + PyMongo CRUD application entrypoint.
Place this file at the project root alongside the `templates/` and `static/` folders.

Run: python app.py
Requires: flask, pymongo
Install: pip install flask pymongo

Environment:
  - MONGO_URI: optional MongoDB connection string (defaults to mongodb://localhost:27017/)
"""

from flask import Flask, render_template, request, redirect, url_for, abort
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['myapp_db']
collection = db['students']

@app.route('/')
def index():
    """List all student documents (convert ObjectId to string)"""
    students = list(collection.find())
    # convert ObjectId to plain string so templates can use student._id directly
    for s in students:
        s['_id'] = str(s['_id'])
    return render_template('index.html', students=students)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        course = request.form.get('course')
        if not name or not age:
            abort(400, 'Name and age are required')
        doc = {'name': name, 'age': int(age), 'course': course}
        collection.insert_one(doc)
        return redirect(url_for('index'))
    return render_template('form.html', student=None, action='Create')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    try:
        oid = ObjectId(id)
    except Exception:
        abort(404)
    student = collection.find_one({'_id': oid})
    if not student:
        abort(404)
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        course = request.form.get('course')
        if not name or not age:
            abort(400, 'Name and age are required')
        collection.update_one({'_id': oid}, {'$set': {'name': name, 'age': int(age), 'course': course}})
        return redirect(url_for('index'))
    # convert _id to string for template
    student['_id'] = str(student['_id'])
    return render_template('form.html', student=student, action='Update')

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    try:
        oid = ObjectId(id)
    except Exception:
        abort(404)
    collection.delete_one({'_id': oid})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
