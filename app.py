import os
import json
from bson import ObjectId
import datetime

from flask import Flask, request, jsonify
from flask_cors import CORS
from src.db import DB

DB.init()
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return f'<h1>Hello world</h1>'

# ANCHOR student


@app.route('/student/all', methods=['GET'])
def studentAll():
    cur = DB.listAllCol("Student")
    d = [i for i in cur]
    return jsonify(d)


@app.route('/student/add', methods=['POST'])
def studentAdd():
    data = request.json
    data['_id'] = data['stud_id']
    DB.insertInto("Student", data)
    return jsonify(data)


@app.route('/student/login', methods=['POST'])
def studentLogin():
    data = request.json
    id = data['stud_id']
    password = data['password']
    try:
        cur = DB.listCol("Student", {"_id": id, "password": password})
        return jsonify(cur[0])
    except:
        return "error"


@app.route('/student/studentSendRequestCourseToTeacher', methods=['POST'])
def studentSendRequestCourseToTeacher():
    data = request.json
    dat = {
        "stud_id": data['stud_id'],
        "detail": "add student to course",
        "course_id": data['course_id'],
        "course_sec": data['course_sec'],
        "time_stamp": datetime.datetime.now()
    }
    prof = DB.listCol("Professor", {"_id": data['prof_id']})[0]
    ann = prof['prof_anouncement']
    ann.append(dat)
    try:
        DB.updateCol("Professor", {"_id": data['prof_id']},
                     {"$set": {"prof_anouncement": ann}})
        return "success"
    except:
        return "error to update "


@app.route('/student/bypassSchedule', methods=['POST'])
def studentBypassSchdule():
    data = request.json
    dat = {
        'stud_id': data['stud_id'],
        'data': data['course']
    }
    DB.insertInto("Schedule", dat)
    dat['_id'] = str(dat['_id'])
    print(dat)
    return jsonify(dat)


@app.route('/student/announcment', methods=['GET'])
def studentViewAnnouncement():
    data = request.json
    course = data['course_id']
    cur = DB.listCol("Announcement", {'ann_course': course})
    return jsonify(cur[0])

# ANCHOR course


@app.route('/course/all', methods=['GET'])
def courseAll():
    cur = DB.listAllCol("Course")
    d = [i for i in cur]
    return jsonify(d)


@app.route('/course/add', methods=['POST'])
def courseAdd():
    data = request.json
    data["_id"]: data['cour_id']
    try:
        DB.insertInto("Course", data)
        return jsonify(data)
    except:
        return "error insert course into database"


@app.route('/course/info', methods=['GET'])
def courseInfo():
    data = request.json
    try:
        cur = DB.listCol("Course", {"_id": data['course_id']})
        return jsonify(cur[0])
    except:
        return "error in course info"


@app.route('/course/infoWithSec', methods=['GET'])
def courseInfoWithSec():
    data = request.json
    try:
        cur = DB.listCol('Course', {"_id": data['course_id']})[0]
        if(data['course_sec'] >= len(cur['course_sec'])):
            return "error sec cannot found"
        return jsonify({
            "course_id": cur['course_id'],
            "course_name": cur['course_name'],
            "course_sec": cur['course_sec'][data['course_sec']-1]
        })
    except:
        return "error to find course"

# ANCHOR teacher


@app.route('/professor/all', methods=['GET'])
def professorAll():
    try:
        cur = DB.listAllCol("Professor")
        d = [i for i in cur]
        return jsonify(d)
    except:
        return "error in professor all"


@app.route('/professor/add', methods=['POST'])
def professorAdd():
    data = request.json
    try:
        data['_id'] = data['prof_id']
        DB.insertInto("Professor", data)
        return jsonify(data)
    except:
        return "error prfessor add"


@app.route('/professor/login', methods=['POST'])
def professorLogin():
    data = request.json
    try:
        cur = DB.listCol(
            "Professor", {"_id": data['prof_id'], "password": data['password']})
        return jsonify(cur[0])
    except:
        return "error"


@app.route('/professor/addAnouncement', methods=['POST'])
def professorAddAnouncement():
    data = request.json
    try:
        data['_id'] = data['ann_id']
        DB.insertInto("Anouncement", data)
        return jsonify(data)
    except:
        return "error add anouncement"


@app.route('/professor/studentToCourse', methods=[''])
def professorStudentToCoiurse():
    data = request.json
    try:
        stu = DB.listCol('Student', {'_id': data['stud_id']})[0]
        course_cur = DB.list('Course', {'_id': data['course_id']})
        course = [i for i in course_cur]
    except:
        return "error to add student to course"


# ANCHOR Schudule Mother Fucker


@app.route('/schudule/', methods=['POST'])
def displaySchedule():
    data = request.json
    data['_id'] = data['stud_id']
    try:
        cur = DB.listCol("Schudule", {"_id": data['stud_id']})
    except:
        return "error"


# ANCHOR admin


@app.route('/admin/addTeacherToCourse', methods=['POST'])
def adminAddTeacherToCorse():
    data = request.json
    course = DB.listCol("Course", {"_id": data['course_id']})[0]

    return 0


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
