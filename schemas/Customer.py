from pydantic import BaseModel
from typing import Optional, List
from database_model import Customer
from typing import Optional
from datetime import datetime, date
from pydantic import BaseModel


class CustomerKeySchema(BaseModel):
    """Defines how a new Customer should be represented"""
    customer_key: int

class CustomerSchema(BaseModel):
    """Defines how a new Customer should be represented"""
    full_name: str
    date_of_birth: date
    e_mail: str
    home_adress: Optional[str] = None
    social_number: str

class CustomerViewSchema(BaseModel):
    """ Define how a new Customer should be returned
    """
    full_name = str
    customer_key = int
    date_of_birth = date
    e_mail = str
    customer_since = datetime
    home_adress = str
    social_number = str

class CustomerSummarySchema(BaseModel):
    """Defines how a customer summary should be represented"""
    customer_key: int
    full_name: str


class CustomersListSchema(BaseModel):
    """Defines how a list of customer summaries should be returned"""
    customers: List[CustomerSummarySchema]

def show_customer_view(customer: Customer):
    """Returns a customer view representation
    """
    return {
        "full_name": customer.full_name,
        "customer_key": customer.customer_key,
        "date_of_birth": customer.date_of_birth.isoformat(),
        "e_mail": customer.e_mail,
        "customer_since": customer.customer_since.isoformat(),
        "home_adress": customer.home_adress,
        "social_number": customer.social_number,
    }


def show_customers_list(customers: List[Customer]):
    """Returns a list representation of customer summaries"""
    return {
        "customers": [
            {"customer_key": customer.customer_key, "full_name": customer.full_name}
            for customer in customers
        ]
    }
