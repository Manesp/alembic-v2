from . import BaseModel
from . import db


class Role(BaseModel):
    __versioned__ = {"strategy": "subquery"}
    __tablename__ = "role"

    id = db.Column(db.BigInteger, primary_key=True)
    role_name = db.Column(db.String(50))


    def serialize(self):
        d = dict()
        d["id"] = self.id
        d["role_name"] = self.role_name
        return d