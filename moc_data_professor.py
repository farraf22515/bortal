from src.db import DB
import random
DB.init()

for i in range(5):
    data = {
        "_id": str(i),
        "prof_id": str(i),
        "password": str(random.randint(100000, 999999)),
        "prof_firstname": f'Prof_f_{i}',
        "prof_lastname": f'prof_l_{i}',
        "prof_course": [],
        "prof_anouncement": []
    }
    print(data)
    DB.insertInto('Professor', data)
