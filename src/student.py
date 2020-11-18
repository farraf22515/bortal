from flask import Blueprint, jsonify, request
import json
from db import DB

student = Blueprint("student", __name__)


@student.route('/all', methods=['GET'])
def students():
    cur = DB.listAllCol("Student")
    d = [i for i in cur]
    return jsonify(d)


@student.route('/addStudent', methods=['POST'])
def addStudent():
    data = request.json
    data['_id'] = int(data["stud_id"])
    DB.insertInto("Student", data)
    print("add data success")
    return jsonify(data)


@student.route('/login', methods=['GET'])
def studentLogin():
    data = request.json
    stu = DB.listCol(
        "Student", {"_id": data["stud_id"], "password": data["password"]})
    return jsonify(stu[0]) if stu else "not found"


@student.route('/getInfo', methods=['GET'])
def getStudentInfo():
    data = request.json()
    stu = DB.listCol("Student", {"_id": data['sud_id']})
    return jsonify(stu[0])
