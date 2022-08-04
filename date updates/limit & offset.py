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

@app.route('/get_limited_data/limite/offset', methods=['GET'])
def get_limited_records1():
    # Limit: How many leads to distribute, offset: Stating point
    result = session.query(Tsr_colleage).limit(2).offset(5).all()
    results_1 = [item.__dict__ for item in result]
    for item in results_1:
        del item['_sa_instance_state']
    return json.dumps(results_1)

app.run(debug=True)
