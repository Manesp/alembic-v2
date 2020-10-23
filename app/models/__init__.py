import sqlalchemy

from ..extensions import db

from . import Cars


sqlalchemy.orm.configure_mappers()