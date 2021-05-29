# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime
from models.database import Base
from datetime import datetime

# 温度とセンサーの現在データテーブル定義
# ここでは温度データ1つ, センサーデータ1つを保存
# テーブル定義は適宜設定してください
class SensorCurrent(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    j_merged_num = Column(Integer)
    z_merged_num = Column(Integer)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, name=None, j_merged_num=None, z_merged_num=None, date=None):
        self.name = name
        self.j_merged_num = j_merged_num
        self.z_merged_num = z_merged_num
        self.date = date

    def __repr__(self):
        return '<Name %r>' % (self.name)