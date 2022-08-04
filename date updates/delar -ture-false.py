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


@app.route('/tsr', methods=['GET'])
def home():
    req = request.args.get("name")
    result = session.query(Tsr_colleage).filter(Tsr_colleage.Stdcode == req)\
                                        .filter(Tsr_colleage.SentToDealer.is_(False)).all()
    print(type(result))
    result_1 = [item.__dict__ for item in result]
    print("------------------------------------->>>>>>>>>>>>",result_1)
    mobileno_container = []
    for item in result_1:
        item.pop('_sa_instance_state')
        mobileno_container.append(item.get('Mobile'))
    enable_sent_flag(mobileno_container)
    return json.dumps(result_1)

def enable_sent_flag(mobileno_container):
    print("Container {}".format(mobileno_container))
    for mobileno in mobileno_container:
        session.query(Tsr_colleage).filter(Tsr_colleage.Mobile == mobileno) \
            .update({'SentToDealer': True},synchronize_session='fetch')
        session.commit()

app.run(debug=True)