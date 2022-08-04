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
from sqlalchemy import and_,or_


app = Flask(__name__)
api = Api(app)
Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5432/postgres"
engine = create_engine(database_url, echo=True, poolclass=NullPool)
Session = sessionmaker(bind=engine)
session = Session()
class tsr1(Base):
    __tablename__ = 'tsr'
    Name = Column("name", String)
    age = Column("age", Integer)
    mobile= Column("mobile", Integer, primary_key=True)
    address = Column("address", String)
#http://127.0.0.1:5000/tsr/update-address?mobile=7097535317&address=tiruapti
@app.route('/tsr/update-address', methods=['PATCH'])
def tsr_update_address():
        mobile = request.args.get('mobile')
        address = request.args.get('address')
        session.query(tsr1).filter(tsr1.mobile == mobile).update({"address": address})
        session.commit()
        return "address has been updated"
app.run(debug=True)