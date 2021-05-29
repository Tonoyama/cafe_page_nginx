# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime
from models.database import Base
from datetime import datetime

class SensorCurrent(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    j_merged_num = Column(Integer)
    z_merged_num = Column(Integer)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, j_merged_num=None, z_merged_num=None, date=None):
        self.j_merged_num = j_merged_num
        self.z_merged_num = z_merged_num
        self.date = date
