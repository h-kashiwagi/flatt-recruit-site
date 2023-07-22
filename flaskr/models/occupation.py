from flaskr import db
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from pytz import timezone
from flaskr import engine



# 職種
class Occupation(db.Model):
    __tablename__ = 'occupation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    companies = db.relationship('Company', backref='occupation')

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