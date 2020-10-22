import sqlalchemy

from ..extensions import db

from .cars import Cars


sqlalchemy.orm.configure_mappers()