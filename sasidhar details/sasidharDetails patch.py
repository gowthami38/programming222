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

class sasidharFmailyDetails(Base):
    __tablename__ = "sasidhardetails"
    name = Column("name", String)
    age = Column("age", Integer)
    salary = Column("salary", Integer)
    address = Column("address", String)
    mobile = Column("mobile", Integer,primary_key=True)
#http://127.0.0.1:5000/sasidhar/fmaily/details?mobile=2345678&address=chittoorupdated
@app.route('/sasidhar/fmaily/details', methods=['PATCH'])
def tsr_update_brand():
        mobileNumber = int(request.args.get('mobile'))
        address = request.args.get('address')
        session.query(sasidharFmailyDetails).filter(sasidharFmailyDetails.mobile == mobileNumber)\
            .update({"address": address})
        session.commit()
        return "address has been updated"
app.run(debug=True)