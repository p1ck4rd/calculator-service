from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ExpressionResult(Base):
    __tablename__ = 'expressions_results'

    id = Column(Integer, primary_key=True)
    result = Column(Float)
