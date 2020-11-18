from flask import Blueprint, jsonify, request
import json
from db import DB

course = Blueprint('professor', __name__)
