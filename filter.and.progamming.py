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
class kgr1(Base):
    __tablename__ = 'kgr'
    Name = Column("name", String)
    age = Column("age", Integer)
    mobile= Column("mobile", Integer, primary_key=True)
    salary = Column("salary",Integer)
#http://127.0.0.1:5000//kgr/filter/and-filter
@app.route('/kgr/filter/and-filter', methods=['GET'])
def home():
    mobileNumber = request.args.get('mobile')
    NameFull=request.args.get('name')
    results = session.query(kgr1).filter(and_(kgr1.mobile == mobileNumber,kgr1.Name ==NameFull)).all()
    results_3=[item.__dict__ for item in results]
    for item in results_3:
        del item['_sa_instance_state']
    return json.dumps(results_3)
app.run(debug=True)
