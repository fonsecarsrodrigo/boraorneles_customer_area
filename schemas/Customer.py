from pydantic import BaseModel
from typing import Optional, List
from database_model import Customer
from typing import Optional
from datetime import date

class CustomerSchema(BaseModel):
    """Defines how a new Customer should be represented"""
    full_name: str
    date_of_birth: str
    e_mail: str
    customer_since: Optional[date] = None
    home_adress: Optional[str] = None

class CustomerViewSchema(BaseModel):
    """ Define how a new Customer should be returned
    """
    full_name = str
    customer_key = int
    date_of_birth = str
    e_mail = str
    customer_since = date
    home_adress = str

def show_customer_view(customer: Customer):
    """Returns a customer view representation
    """
    return {
        "full_name": customer.full_name,
        "customer_key": customer.customer_key,
        "date_of_birth": customer.date_of_birth,
        "e_mail": customer.e_mail,
        "customer_since": customer.customer_since.isoformat(),
        "home_adress": customer.home_adress,
    }