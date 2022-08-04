
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

class Tsr_colleage(Base):
    __tablename__ = "tsr_colleage"
    Namestd = Column("name_std", String)
    Agestd = Column("age_std", Integer)
    Salary = Column("salary", Integer)
    City = Column("city", String)
    Mobile = Column("mobile", Integer,primary_key=True)
    Create_date=Column("create_date", String)
    SentToDealer = Column("senttodealer", BOOLEAN)
    Stdcode = Column("stdcodem", String )


@app.route('/tsr_colleage/true/false', methods=['GET'])
def home():
    stdcodeTSR = request.args.get("stdcodem")
    result = session.query(Tsr_colleage).\
             filter(Tsr_colleage.SentToDealer == 'False',
            Tsr_colleage.Stdcode == stdcodeTSR).all()
    print(type(result))
    resulttsr = [item.__dict__ for item in result]
    mobileno_container = []
    for item in resulttsr:
        item.pop('_sa_instance_state')
        mobileno_container.append(item.get('Mobile'))
    enable_sent_flag(mobileno_container)
    return str(resulttsr)


def enable_sent_flag(mobileno_container):
    print("Container {}".format(mobileno_container))
    for mobileno in mobileno_container:
        session.query(Tsr_colleage).filter(Tsr_colleage.Mobile == mobileno) \
            .update({"SentToDealer": True})
        session.commit()

app.run(debug=True)