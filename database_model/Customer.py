from sqlalchemy import Column, Integer, String, Date
from datetime import date
from typing import Union

from database_model.base import Base

class Customer(Base):
    __tablename__ = 'customer'
    full_name = Column(String)
    customer_key = Column(Integer, primary_key=True, autoincrement=True)
    date_of_birth = Column(Date, default=date.min)
    e_mail = Column(Integer)
    customer_since = Column(Date, default=date.today)
    home_adress = Column(String)

    def __init__(
        self,
        full_name: str,
        date_of_birth: date,
        e_mail: int,
        home_adress: str,
        customer_since: Union[Date, None] = None,
    ):
        """
        Creates a Customer

        Arguments:
            full_name: customer's full name
            date_of_birth: customer's date of birth
            e_mail: customer's email (as defined in the SQL schema)
            customer_since: date since when the customer has been registered
            home_adress: customer's home address
        """
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.e_mail = e_mail
        self.home_adress = home_adress

        # if not provided, it will default to today's date
        if customer_since:
            self.customer_since = customer_since
