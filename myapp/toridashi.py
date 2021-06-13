from flask import Flask, render_template, request, json, jsonify
from models.models import SensorCurrent
from models.database import db_session

print("実行中...")

users = db_session.query(SensorCurrent).all()

for user in users:
    j = user.j_merged_num
    z = user.z_merged_num
    date = user.date
    print(j, z, date.strftime('%Y-%m-%d %H:%M:%S'))