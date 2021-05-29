# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, json, jsonify
from models.models import SensorCurrent
from models.database import db_session

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
    return render_template('index.html', addr2=addr2)

@app.route("/3", methods=['POST'])
def info3():
    global addr3
    addr3 = str(request.form['addr3'])
    addr3 = addr3.split()
    addr3 = set(addr3)
    return render_template('index.html', addr3=addr3)

@app.route("/", methods=["GET"])
def view():
    counted = len(list(addr | addr2))
    counted_2 = len(addr3)

    current = SensorCurrent.query.first()
    current.j_merged_num = counted
    current.z_merged_num = counted_2
    db_session.commit()
    db_session.close()

    data = SensorCurrent.query.first()
    print("\n-------------")
    print(data)
    print("-------------\n")
    return render_template('index.html', people=data)

# Ajax処理
@app.route("/people", methods=['POST'])
def getCurrData():
    # SQliteから温度とセンサーの現在データを取得
    people = SensorCurrent.query.first()
    # JSONに変換して結果を返す
    json_data = {
        'j_merged_num': people.j_merged_num,
        'z_merged_num': people.z_merged_num
    }
    return jsonify(Result=json.dumps(json_data))

if __name__ == "__main__":
    app.run()