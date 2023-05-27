from sqlalchemy import Column, Integer, String, Date, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = 'flights'
    
    ''' Flight table columns '''
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    departure = Column(String(255), nullable=False)
    destination = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

class Booking(Base):
    __tablename__ = 'bookings'
    
    ''' Booking table columns '''
    id = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey('flights.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(String(255), nullable=False)
    
    ''' Relationship with Flight and User tables '''
    flight = relationship("Flight", backref="bookings")
    user = relationship("User", backref="bookings")

class User(Base):
    __tablename__ = 'users'
    
    ''' User table columns '''
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
