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


# @app.route('/TsrColleage/date/update', methods=['GET'])
# def home():
#     results = session.query(Tsr_colleage).all()
#     results_1 = [item.__dict__ for item in results]
#     for item in results_1:
#         del item['_sa_instance_state']
#     return json.dumps(results_1)
# app.run(debug=True)

# http://127.0.0.1:5000/TsrColleage/date/update?startdate=2019-01-01&enddate=2019-01-07
@app.route('/TsrColleage/date/update', methods=['GET'])
def home():
    start_date = request.args.get("startdate")
    end_date = request.args.get("enddate")
    # result = session.query(Tsr_colleage).filter(Tsr_colleage.CreatedDate >= 2022-1-1).all()
    #
    # result = session.query(Tsr_colleage). \
    #     filter(Tsr_colleage.CreatedDate >= 2022 - 1 - 1,
    #            Tsr_colleage.CreatedDate < 2022 - 3 - 1).all()

    result = session.query(Tsr_colleage). \
        filter(Tsr_colleage.Create_date >= start_date,
               Tsr_colleage.Create_date < end_date).all()
    results_1 = [item.__dict__ for item in result]
    for item in results_1:
        del item['_sa_instance_state']
    return json.dumps(results_1)

app.run(debug=True)