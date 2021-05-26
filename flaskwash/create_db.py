from flaskwash import db
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(80))

    def __init__(self, first_name, last_name, email,phone_numer):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_numer = phone_numer

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.Unicode(255))
    plate_number = db.Column(db.String(80), nullable=False)
    vehicle_brand = db.Column(db.String(80), nullable=False)

    def __init__(self, first_name, last_name, email,phone_numer, plate_number, vehicle_brand):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_numer = phone_numer
        self.plate_number = plate_number
        self.vehicle_brand = vehicle_brand


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80), nullable=False)
    item_qty = db.Column(db.SmallInteger, nullable=False)
    item_price = db.Column(db.SmallInteger, nullable=False)
    total_inventory = db.Column(db.SmallInteger, nullable=False)
    #report_id = relationship('Report')
    def __init__(self, item_name, item_qty, item_price, total_inventory):
        self.item_name = item_name
        self.item_qty = item_qty
        self.item_price = item_price
        self.total_inventory = total_inventory

# class Report(db.Model):
#     #Sales = number items sold
#     id = db.Column(db.Integer, primary_key=True)
#     name = Column(db.Integer, ForeignKey('Item.item_name'))
#     item_qty = Column(db.Integer, ForeignKey('Item.item_qty'))
#     item_price = Column(db.Integer, ForeignKey('Item.item_price'))
    
#     def __init__(self, name, item_qty, item_price):
#         self.name = name
#         self.item_qty = item_qty
#         self.item_price = item_price
    

