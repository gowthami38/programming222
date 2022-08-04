import json
from datetime import datetime
import psycopg2
from flask import Flask
from flask_restful import Api, request
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
class hero1(Base):
    __tablename__ = 'enquiry_test_ride'
    customeName = Column("customer_name", String)
    mobileNo = Column("mobile_no", Integer, primary_key=True)
    vehicleModelm = Column("vehicle_modelm", Integer)
    states = Column("states", String)
    district = Column("district", String)
    city = Column("city", String)
    existingVehicle = Column("existing_vehicle", Integer)
    dealerState = Column("dealer_state", String)
    dealerTown = Column("dealer_town", String)
    dealer = Column("dealer",String)
    briefAboutEnquiry = Column("brief_about_enquiry", String)
    expectedDateOfPurchase = Column("expected_date_of_purchase",Integer)
    gender = Column("gender",String)
    age = Column("age", Integer)
    occupation = Column("occupation", String)
    intendedUsage = Column("intended_usage",String)

class NewCustomerDetails(Base):
    __tablename__ = "customer_details5"
    customeNrame = Column("customer_name", String)
    age = Column("age", Integer)
    gender = Column("gender",String)
    mobile = Column("mobile_no", Integer, primary_key=True)
    dealerState = Column("dealer_state", String)
    is_new_customer= Column("is_new_customer", BOOLEAN)

# http://127.0.0.1:5000/update/dealerstate/address?mobile=999999&dealerState=Andhar pradhesh
@app.route('/update/dealerstate/address', methods=['PATCH'])
def update_dealerstate():
    mobile_tsr = int(request.args.get('mobile'))
    dealer_state = request.args.get('dealerState')
    session.query(hero1).filter(hero1.mobileNo == mobile_tsr) \
        .update({'dealerState': dealer_state})
    session.commit()
    new_customer_status(mobile_tsr)

    return {"mobile":mobile_tsr,"status": "updated", "error": "noo"}

def new_customer_status(mobile1):
    customer_name_full_new = session.query(hero1.customeName).filter(hero1.mobileNo == mobile1).all()
    session.query(NewCustomerDetails).filter(NewCustomerDetails.customeNrame == customer_name_full_new[0][0]) \
        .update({'is_new_customer': False})
    session.commit()



app.run(debug=True)
