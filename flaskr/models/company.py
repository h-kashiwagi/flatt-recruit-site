from flaskr import db
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from pytz import timezone
from flaskr import engine


# 中間テーブル
class Tags(db.Model):

    __tablename__ = "tags"

    company_id = db.Column(db.Integer, db.ForeignKey("company.id"), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), primary_key=True)

# 会社
class Company(db.Model):
    __tablename__ = 'company'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(128))
    # 外部キー
    industry_id = db.Column(db.Integer, db.ForeignKey('industry.id', onupdate='CASCADE', ondelete='CASCADE'))
    # 外部キー
    occupation_id = db.Column(db.Integer, db.ForeignKey('occupation.id', onupdate='CASCADE', ondelete='CASCADE'))
    # 親
    relations = db.relationship('Relation', backref='company')
    # 親
    images = db.relationship('Image', backref='company')
    # 1対1
    manager = db.relationship('Manager', backref='company', uselist=False)
    # 1対1
    condition = db.relationship('Condition', backref='company', uselist=False)
    # 多対多
    tags = db.relationship('Tag', secondary=Tags.__tablename__, back_populates='companies')
    work_location = db.Column(db.String(128))
    job_role = db.Column(db.Text)
    ideal = db.Column(db.String(128))
    anuual_income = db.Column(db.Integer) 
    monthly_income = db.Column(db.Integer)
    url = db.Column(db.String(128))
    capital = db.Column(db.Integer)
    established = db.Column(db.String(64))
    employees = db.Column(db.Integer)
    head_office = db.Column(db.String(128))
    representative = db.Column(db.String(64))
    business_content = db.Column(db.Text)
    message = db.Column(db.Text)
    is_published = db.Column(db.Boolean)
    del_flg = db.Column(db.Boolean)
    created_at = db.Column('created', db.DateTime, default=datetime.now(timezone('Asia/Tokyo')).replace(second=0, microsecond=0), nullable=False)
    updated_at = db.Column('modified',db.DateTime, default=datetime.now(timezone('Asia/Tokyo')).replace(second=0, microsecond=0), nullable=False)

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'industry_id': self.industry_id,
            'occupation_id': self.occupation_id,
            'work_location': self.work_location,
            'job_role': self.job_role,
            'ideal': self.ideal,
            'anuual_income': self.anuual_income,
            'monthly_income': self.monthly_income,
            'url': self.url,
            'capital': self.capital,
            'established': self.established,
            'employees': self.employees,
            'head_office': self.head_office,
            'representative': self.representative,
            'business_content': self.business_content,
            'message': self.message,
            'is_published': self.is_published,
            'del_flg': self.del_flg,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

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
    
    
# タグ
class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    companies = db.relationship('Company', secondary=Tags.__tablename__, back_populates="tags")

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
