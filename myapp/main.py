# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, json, jsonify, Response
from models.models import SensorCurrent
from models.database import db_session
from datetime import datetime
import random
import time

app = Flask(__name__)

@app.route("/", methods=['POST'])
def info():
    global addr
    addr = str(request.form['addr'])
    addr = addr.split()
    addr = set(addr)
    return render_template('index.html', addr=addr)

@app.route("/2", methods=['POST'])
def info2():
    global addr2
    addr2 = str(request.form['addr2'])
    addr2 = addr2.split()
    addr2 = set(addr2)
    counted = len(list(addr | addr2))
    counted = counted + random.randint(110, 200)
    counted = int((counted - 109.25) / 0.7366)

    if counted < 0:
        counted = 0

    current = SensorCurrent.query.first()
    current.j_merged_num = counted
    db_session.commit()
    db_session.close()
    return render_template('index.html', addr2=addr2)

@app.route("/3", methods=['POST'])
def info3():
    global addr3
    addr3 = str(request.form['addr3'])
    addr3 = addr3.split()
    addr3 = set(addr3)
    counted_2 = len(addr3)
    counted_2 = counted_2 + random.randint(110, 200)
    counted_2 = int((counted_2 - 109.25) / 0.7366)

    if counted_2 < 0:
        counted_2 = 0

    current = SensorCurrent.query.first()
    current.z_merged_num = counted_2
    db_session.commit()
    db_session.close()
    return render_template('index.html', addr3=addr3)

@app.route("/")
def index():
    people = SensorCurrent.query.first()
    return render_template('index.html', people=people)

# Ajax処理
@app.route("/people", methods=['POST'])
def getCurrData():
    people = SensorCurrent.query.first()

    json_data = {
        'j_merged_num': people.j_merged_num,
        'z_merged_num': people.z_merged_num
    }
    return jsonify(Result=json.dumps(json_data))

def generate_random_data():
    user_data = SensorCurrent.query.first()
    user_data.j_merged_num = user_data.j_merged_num
    user_data.z_merged_num = user_data.z_merged_num
    user_data.date = datetime.now()
    db_session.commit()
    db_session.close()

    users = db_session.query(SensorCurrent).all()

    for user in users:
        j = user.j_merged_num
        z = user.z_merged_num
        date = user.date
        print(j, z, date.strftime('%Y-%m-%d %H:%M:%S'))

    data = SensorCurrent.query.first()
    json_data = json.dumps(
        {
            "time": datetime.now().strftime("%H:%M"),
            "j_value": data.j_merged_num,
            "z_value": data.z_merged_num,
        }
    )
    yield f"data:{json_data}\n\n"

@app.route("/chart-data")
def chart_data():
    time.sleep(20)
    return Response(generate_random_data(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(threaded=True)