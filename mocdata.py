import random
import string
from src.db import DB

DB.init()


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return result_str


for i in range(100):
    studentID = str(random.randint(6133701623, 6133762823))
    password = str(random.randint(1234, 4567))
    stud_Fname = get_random_string(8)
    stud_grade = random.randint(200, 400)/100
    stud_Lname = get_random_string(8)
    stud_prof = '0'
    data = {
        "_id": studentID,
        "password": password,
        "stud_course": [],
        "stud_firstname": stud_Fname,
        "stud_grade": stud_grade,
        "stud_id": studentID,
        "stud_lastname": stud_Lname,
        "stud_prof": stud_prof,
        "stud_schedule": []
    }
    DB.insertInto('Student', data)
    print(data)
