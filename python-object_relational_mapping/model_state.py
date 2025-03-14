#!/usr/bin/python3
"""Model definition for State class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# create the base class for declarative models
Base = declarative_base()

class State(Base):
    """State class that inherits from Base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
