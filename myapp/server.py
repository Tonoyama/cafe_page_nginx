# -*- coding: utf-8 -*-

from flask import Flask
from main import app
from models.database import init_db

if __name__ == "__main__":
    # Database初期化
    init_db()
    # アプリ起動(host=0,0,0,0で全てのアクセス許可)
    app.run(host='0.0.0.0', debug=True)