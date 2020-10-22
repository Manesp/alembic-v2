from . import db
from datetime import datetime
from app.extensions import activity_plugin
from flask import current_app
from sqlalchemy.types import Boolean
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy_continuum import version_class
import json
import sqlalchemy
import re
from enum import Enum
from sqlalchemy.orm import mapper
from sqlalchemy import event

class BaseModel(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # status = db.Column(db.String(20), default='active')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)