from src.db import DB
import random

DB.init()
k = str(random.randint(21, 30)) + "0" + str(random.randint(100, 200))
data = {
    "_id": str(k),
    "course_name": "Course",
    "course_id": str(k),
    "course_sec": [{
        "sec": str(random.randint(1, 4)),
        "time": [],
        "prof": [],
        "classroom": "",
        "stud": [],
        "ann": []
    }],
    "course_description": """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Suspendisse odio sem, ullamcorper sed pellentesque vitae, 
        consequat nec orci. Nulla eu massa at felis vulputate dapibus. 
        Fusce fermentum velit felis, efficitur pellentesque tortor 
        dapibus in. Nullam ex odio, lobortis eu fermentum a, vulputate 
        sit amet enim. Vivamus suscipit dui magna, a commodo odio 
        ornare eget. Vivamus eu tellus quis ex porttitor dapibus eu eu 
        sem. Etiam efficitur nec nisi tincidunt commodo.
    """,
    "course_midterm": "",
    "course_final": ""
}

for i in range(50):
    c_id = str(random.randint(21, 30))+"01" + str(random.randint(10, 99))
    c_sec = random.randint(1, 3)
    data['course_id'] = c_id
    data['course_name'] = "course_" + str(i)
    data['_id'] = c_id
    data['course_sec'] = []
    prof = "0"
    for i in range(c_sec):
        time1 = random.randint(1, 7)
        time2 = random.randint(8, 13)
        time2s = str(time2)
        if(time2 < 10):
            time2s = "0" + str(time2)
        time3 = time2 + 3
        time = str(time1) + time2s + "00" + str(time3) + "00"
        classroom = str(random.randint(200, 217))
        k = {
            'sec': i+1,
            'time': [time],
            'prof': '0',
            'classroom': classroom,
            'stud': [],
            'ann': [],
            'prof': prof
        }
        data['course_sec'].append(k)
    DB.insertInto('Course', data)
    print(data)
