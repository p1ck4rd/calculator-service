from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .model import Base, ExpressionResult

engine = create_engine('postgresql://postgres:postgres@db/calculator')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


class DataBase:
    def __init__(self):
        self._session = Session()

    def __del__(self):
        self._session.close()

    def save_result(self, result):
        new_result = ExpressionResult(result=result)
        try:
            self._session.add(new_result)
            self._session.commit()
        except:
            self._session.rollback()
            raise
        return new_result.id

    def get_result(self, result_id):
        return self._session.query(ExpressionResult.result).filter(
            ExpressionResult.id == result_id).one()[0]
