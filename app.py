import os
import json
from flask import Flask, request, jsonify

from src.db import DB
from src.student import student

DB.init()
app = Flask(__name__)
app.register_blueprint(student, url_prefix="student")


@app.route('/')
def index():
    return f'<h1>Hello world</h1>'
# Course


@app.route('/course', methods=['GET'])
def subjects():
    cur = DB.listALlCol("Course")
    d = [i for i in cur]
    return jsonify(d)


@app.route('/course/getCOurseInfo', methods=['GET'])
def getCourseInfo():
    cur = DB.listCol("")


@ app.route('/course/addCourse', methods=['POST'])
def addCourse():
    data = request.json
    data["_id"] = data.course_id
    DB.insertInto("Course", data)
    print("add course success")
    return jsonify(data)


# Professor
@ app.route('/professor', methods=['GET'])
def professors():
    cur = DB.listAllCol("Professor")
    d = [i for i in cur]
    return jsonify(cur)

# Announcement


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
