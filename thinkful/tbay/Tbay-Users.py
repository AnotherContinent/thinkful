from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tbay import User, Item, Bid, session, Base

engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

beyonce = User(username="bknowles", password="crazyinlove")
session.add(beyonce)
session.commit()

