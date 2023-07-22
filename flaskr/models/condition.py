from flaskr import db
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from pytz import timezone
from flaskr import engine



# 条件
class Condition(db.Model):
    __tablename__ = 'condition'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    # unique制約によって1対1を保証
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), unique=True)

    # 登録
    def insertData(self):
        Session = sessionmaker(bind=engine)
        ses = Session()
        ses.add(self)
        ses.commit()
        ses.close()
        return

    # 全件
    @classmethod
    def getAll(cls):
        Session = sessionmaker(bind=engine)
        ses = Session()
        res = ses.query(cls).all()
        ses.close()
        return res 

