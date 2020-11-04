import os
import json
from bson import ObjectId
from flask import Flask, request, jsonify
from db import DB

DB.init()
app = Flask(__name__)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return JSONEncoder.default(self, o)


@app.route('/')
def index():
    return f'Hello world'

# Student
@app.route('/student/addStudent', methods=['POST'])
def addStudent():
    data = request.json
    DB.insertInto("Student", data)
    print("add data success")
    return data


@app.route('/student/login', methods=['GET'])
def login():
    data = request.json
    cur = DB.listCol(
        "Student", {"_id": data['_id'], "password": data['password']})
    print("login success")
    return cur[0]

# Subject
@app.route('/subject/addSubject', methods=['POST'])
def addSubject():
    data = request.json
    DB.insertInto("Subject", data)
    print(f'add subject success')
    return data


@app.route('/subject/addStudentToSubject', methods=['POST'])
def addStudentToSubject():
    data = request.json
    sub = DB.listCol("Subject", {"_id": {"$in": data['subjects']}})
    print(*sub)
    return f'hello world'


@app.route('/subject/getTimeSubject', methods=['GET'])
def getTimeSubject():
    data = request.json
    sub = DB.listCol("Subject", {"_id": data['sub_id']})[0]
    for j in sub['learn']:
        if j['sec'] == data['sec']:
            return j
    return 'not sec'


# teacher
@app.route('/teacher/addTeacher', methods=['POST'])
def addTeacher():
    data = request.json
    DB.insertInto("Teacher", data)
    print(f'add teacher success')
    return data


app.run()
