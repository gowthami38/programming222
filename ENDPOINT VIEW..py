import json
from datetime import datetime
import psycopg2
from flask import Flask, request
from flask_restful import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

app = Flask(__name__)
api = Api(app)
Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5432/postgres"
engine = create_engine(database_url, echo=True, poolclass=NullPool)
Session = sessionmaker(bind=engine)
session = Session()

class sasidharCompany(Base):
    __tablename__ = "sasidhar_company"
    Name = Column("name", String)
    Age = Column("age", Integer)
    Emailid = Column("emailid", String)
    Address = Column("address", String)
    Salary = Column("salary", Integer)
    Mobile = Column("mobile", Integer, primary_key=True)
    Is_paid_pfo = Column("is_paid_pfo", String)
# http://127.0.0.1:5000/sasidharCompany/pf
@app.route('/sasidharCompany/pf', methods=['GET'])
def sasidharCompany_pf_updates():
    result = session.query(sasidharCompany).all()
    results_1 = [item.__dict__ for item in result]
    for item in results_1:
        del item['_sa_instance_state']
    return json.dumps(results_1)
# http://127.0.0.1:5000/sasidharCompany/pf/upated?mobile=1234567890&pf=yes
@app.route('/sasidharCompany/pf/upated', methods=['GET'])
def sasidharCompany_pf_updates_1():
    mobile = int(request.args.get('mobile'))
    fee_paid = request.args.get('pf')
    result = session.query(sasidharCompany).filter(sasidharCompany.Mobile==mobile)\
               .update({'Is_paid_pfo':fee_paid})
    session.commit()
    return {'mobile':mobile, "status":"pf_amount_is_updated", "error":"no"}
# http://127.0.0.1:5000//sasidharCompany/pf/view/yes/only
@app.route('/sasidharCompany/pf/view/yes/only', methods=['GET'])
def sasidharCompany_pf_updates3():
    result = session.query(sasidharCompany).filter(sasidharCompany.Is_paid_pfo=='yes').all()
    results_1 = [item.__dict__ for item in result]
    for item in results_1:
        del item['_sa_instance_state']
    return json.dumps(results_1)
# http://127.0.0.1:5000//sasidharCompany/pf/view/no/only
@app.route('/sasidharCompany/pf/view/no/only', methods=['GET'])
def sasidharCompany_pf_updates4():
    result = session.query(sasidharCompany).filter(sasidharCompany.Is_paid_pfo=='no').all()
    results_1 = [item.__dict__ for item in result]
    for item in results_1:
        del item['_sa_instance_state']
    return json.dumps(results_1)
app.run(debug=True)