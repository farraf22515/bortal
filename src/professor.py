from flask import Blueprint, jsonify, request
import json
from src.db import DB

teacher = Blueprint("professor", __name__)


@student.route('/all', methods=['GET'])
def students():
    cur = DB.listAllCol("Student")
    d = [i for i in cur]
    return jsonify(d)
