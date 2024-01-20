from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


class Post(Base):
    __tablename__ = "meds"

    id = Column(Integer, primary_key=True, nullable=False)
    name= Column(String, nullable=False)
    type= Column(String, nullable=False)
    dosage= Column(Integer, nullable=False)
    dosage_unit= Column(String, nullable=False)
    frequency= Column(Integer, nullable=False)
    frequency_unit= Column(String, nullable=False)
    remark= Column(String, server_default='None')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))