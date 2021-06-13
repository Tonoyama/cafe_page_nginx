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
    counted = int(counted / 0.7366)
    print(counted)

    if counted < 0:
        counted = 0

    current = SensorCurrent.query.first()
    current.j_merged_num = int(counted)
    db_session.add(current)
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
    counted_2 = counted_2
    counted_2 = int(counted_2 / 0.7366)
    print("/3 の値：" + str(counted_2))

    if counted_2 < 0:
        counted_2 = 0

    current_2 = SensorCurrent.query.first()
    current_2.z_merged_num = int(counted_2)
    db_session.add(current_2)
    db_session.commit()
    return render_template('index.html', addr3=addr3)

@app.route("/")
def index():
    people = SensorCurrent.query.first()
    return render_template('index.html', people=people)

# Ajax処理
@app.route("/people", methods=['POST'])
def getCurrData():
    users = db_session.query(SensorCurrent).first()

    j = users.j_merged_num
    z = users.z_merged_num
    date = datetime.now()

    print(j, z, date)
    data = SensorCurrent(j ,z , date)

    db_session.add(data)
    db_session.commit()
    db_session.close()
    people = SensorCurrent.query.first()

    json_data = {
        'j_merged_num': people.j_merged_num,
        'z_merged_num': people.z_merged_num
    }

    print(json_data)
    return jsonify(Result=json.dumps(json_data))

def generate_random_data():
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
    time.sleep(5)
    return Response(generate_random_data(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(threaded=True)