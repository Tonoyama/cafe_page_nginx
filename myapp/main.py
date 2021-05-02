# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def info():
    global count, addr
    count = str(request.form['count'])
    addr = str(request.form['addr'])
    return render_template('index.html', count=count, addr=addr)

@app.route("/2", methods=['POST'])
def info2():
    global count2, addr2
    count2 = str(request.form['count2'])
    addr2 = str(request.form['addr2'])
    return render_template('index.html', count2=count2, addr2=addr2)

@app.route("/3", methods=['POST'])
def info3():
    global count3, addr3
    count3 = str(request.form['count3'])
    addr3 = str(request.form['addr3'])
    return render_template('index.html', count3=count3, addr3=addr3)


@app.route("/", methods=["GET"])
def view():
    counted = int(count)+int(count2)
    return render_template('index.html', counted=counted, count2=count3)


if __name__ == "__main__":
    app.run()