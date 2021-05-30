from flask import Flask, render_template, request, json, jsonify
from models.models import SensorCurrent
from models.database import db_session

print("レコード削除中...")
db_session.query(SensorCurrent).delete()
db_session.commit()
db_session.close()

print("削除完了")
print("初期データ挿入中...")

# 初期データ
data = SensorCurrent(25,30)
db_session.add(data)
db_session.commit()
db_session.close()

print("挿入完了")