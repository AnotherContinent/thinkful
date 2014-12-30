from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    seller_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_bid = relationship("Bid", backref="item")
    
class User(Base):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True)
  username = Column(String, nullable=False)
  password = Column(String, nullable=False)
  items = relationship("Item", backref= "seller")
  bids = relationship("Bid", backref = "bidder")
  
class Bid(Base):
  __tablename__ = "bids"
  
  id = Column(Integer, primary_key=True)
  price = Column(Float(precision=3), default=0, nullable=False)

  bidder_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
  
Base.metadata.create_all(engine)

if __name__ == "__main__":
  jesse = User(username="jpinkman", password="chilipowder")
  walter = User(username="walterwhite", password="chemistry")
  skyler = User(username="skywhite", password="boring")
  session.add_all([jesse, walter, skyler])
  session.commit()
  
  baseball = Item(name="baseball", description = "toy", seller = jesse)
  session.add(baseball)
  session.commit()
  
  walter_bid1 = Bid(price = 5, item = baseball, bidder = walter)
  skyler_bid1 = Bid(price = 6, item = baseball, bidder = skyler)
  walter_bid2 = Bid(price = 7, item = baseball, bidder = walter)
  skyler_bid2 = Bid(price = 8, item = baseball, bidder = skyler)
  session.add_all([walter_bid1, skyler_bid1, walter_bid2, skyler_bid2])
  session.commit()
  
  print "The winner is: ", session.query(Bid).order_by(Bid.price).first().bidder.username

    
