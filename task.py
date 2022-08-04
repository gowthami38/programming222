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
    mobile = Column("mobile", Integer, primary_key=True)
    Is_salary_paid = Column("is_salary_paid", BOOLEAN)


@app.route('/create-record', methods=['POST'])
def insert_records():
    try:
        request_body_tsr = request.get_json(force=True)
        for item in request_body_tsr:
            record = ysr(Name=item.get("name"),
                         mobile=item.get("mobile"),
                         Age=item.get("age"))
            session.add_all([record])
        session.commit()

        return {"status": "Success"}
    except Exception as err:
        session.rollback()
        return {"status": "Failed", "msg": str(err)}


app.run(debug=False)

# class CustomerDetails(Base):
#     __tablename__ = "customer_details2"
#     CustomerName = Column("name", String)
#     Age = Column("age", Integer)
#     Address = Column("address", String)
#     mobile = Column("mobile", Integer, primary_key=True)
#     IsNewCustomer = Column("isnewcustomer", BOOLEAN)
#
#
# # http://127.0.0.1:5000/update-fee?mobile=9618115355&Address=chittoor
# @app.route('/update-fee', methods=['PATCH'])
# def update_fee_info():
#     mobile_tsr = int(request.args.get('mobile'))
#     address = request.args.get('Address')
#     session.query(ysr).filter(ysr.mobile == mobile_tsr) \
#         .update({'Address': address})
#     session.commit()
#     set_customer_status(mobile_tsr)
#
#     return {"mobile": mobile_tsr, "status": "updated", "error": "noo"}
#
#
# def set_customer_status(mobile1):
#     customer_name_full = session.query(ysr.Name).filter(ysr.mobile == mobile1).all()
#     session.query(CustomerDetails).filter(CustomerDetails.CustomerName == customer_name_full[0][0]) \
#         .update({'IsNewCustomer': False})
#     session.commit()


#
# @app.route('/fetch-new-leads', methods=['GET'])
# def get_new_leads():
#     request_name = request.args.get("name")
#     result = session.query(ysr).filter(and_(ysr.Name == request_name ,ysr.Is_salary_paid == False)).all()
#     result = [item.__dict__ for item in result]
#     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",result)
#     mobileno_container = []
#     for item in result:
#         print("item is *******************>>>>>>>>>>>",item.get('mobileNumber'))
#         item.pop('_sa_instance_state')
#         mobileno_container.append(item.get('Mobile'))
#     print("mobileno_container----------------------->>>>>>>>",mobileno_container)
#     enable_sent_flag(mobileno_container)
#
#     return json.dumps(result)
#
#
# def enable_sent_flag(mobileno_container):
#     print("Container {}".format(mobileno_container))
#     for mobileno in mobileno_container:
#         print("mobile no-------------------------------------->>>>>>>>>",mobileno)
#         session.query(ysr).filter(ysr.Mobile == mobileno)\
#                                      .update({'Is_salary_paid': True})
#
#         session.commit()
