#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 12:51:43 2018

@author: rohanbagwe
"""
import sys
sys.path.append('/home/rohanbagwe/Google/Flask+SQLAlchemy/User_login/')
from base import Base

from sqlalchemy import Column, Integer, String, Sequence, UniqueConstraint


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))
    UniqueConstraint(username, name="username unique index")
    
    def __repr__(self):
        return "<User(username='%s', fullname='%s', password='%s')>" % (
                                self.username, self.fullname, self.password)
