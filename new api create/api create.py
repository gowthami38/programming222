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

class ysr(Base):
    __tablename__ = "ysr"
    Name = Column("name", String)
    Age = Column("age", Integer)
    Address = Column("address", String)
    Salary = Column("salary", Integer)
    Mobile = Column("mobile", Integer,primary_key=True)
    Is_salary_paid = Column("is_salary_paid", BOOLEAN)


@app.route('/fetch-new-leads', methods=['GET'])
def get_new_leads():
    request_name = request.args.get("name")
    result = session.query(ysr).filter(and_(ysr.Name == request_name ,ysr.Is_salary_paid == False)).all()
    result = [item.__dict__ for item in result]
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",result)
    mobileno_container = []
    for item in result:
        print("item is *******************>>>>>>>>>>>",item.get('mobileNumber'))
        item.pop('_sa_instance_state')
        mobileno_container.append(item.get('Mobile'))
    print("mobileno_container----------------------->>>>>>>>",mobileno_container)
    enable_sent_flag(mobileno_container)

    return json.dumps(result)


def enable_sent_flag(mobileno_container):
    print("Container {}".format(mobileno_container))
    for mobileno in mobileno_container:
        print("mobile no-------------------------------------->>>>>>>>>",mobileno)
        session.query(ysr).filter(ysr.Mobile == mobileno)\
                                     .update({'Is_salary_paid': True})

        session.commit()
app.run(debuge=True)