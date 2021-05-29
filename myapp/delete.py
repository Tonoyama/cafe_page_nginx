from flask import Flask, render_template, request, json, jsonify
from models.models import SensorCurrent
from models.database import db_session

print("全レコード削除")
db_session.query(SensorCurrent).delete()
db_session.commit()
db_session.close()