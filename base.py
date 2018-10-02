#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:29:20 2018

@author: rohanbagwe
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:////home/rohanbagwe/Google/Flask+SQLAlchemy/User_login/users.db', echo=True)

Base = declarative_base()

SessionMakerObj = sessionmaker(bind=engine)
