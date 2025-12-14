from flask import Flask
from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag

from database_model.Customer import Customer
from database_model.TravelPlan import TravelPlan
from database_model import Session

from schemas.Customer import (
    CustomerViewSchema,
    CustomerSchema,
    CustomerKeySchema,
    CustomersListSchema,
    show_customer_view,
    show_customers_list,
)
from schemas.TravelPlan import (
    TravelPlanSchema,
    TravelPlanViewSchema,
    TravelPlanKeySchema,
    show_travel_plan_view,
)
from schemas.error import ErrorSchema
from sqlalchemy.exc import NoResultFound

info = Info(title="Bora Orneles Customer Area API", version="1.0.0")
app = OpenAPI(__name__, info=info)

customer_tag = Tag(name="Customer", description="Add customer to database")
customer_key = Tag(name="CustomerKey", description="Get customer from database key")
travel_plan_tag = Tag(name="TravelPlan", description="Add travel plan to database")

@app.route("/")
def home():
     return redirect('/openapi')

# ------------------------------------------------------------
# Customer Routes
# ------------------------------------------------------------

@app.post('/add_customer',
          tags=[customer_tag],
          responses={"200": CustomerViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_customer(form: CustomerSchema):

    """Add a new customer to the database."""
    customer = Customer(
        full_name=form.full_name,
        date_of_birth=form.date_of_birth,
        e_mail=form.e_mail,
        home_adress=form.home_adress,
        social_number=form.social_number,
        travel_plan_id=form.travel_plan_id,
        )

    # criando conexão com a base
    session = Session()
    # adicionando produto
    session.add(customer)
    # efetivando o camando de adição de novo item na tabela
    session.commit()
    return show_customer_view(customer), 200

@app.get('/get_customers',
         tags=[customer_tag],
         responses={"200": CustomersListSchema})
def get_customers():
    """Get all customers with their identifiers and names."""

    session = Session()
    customers = session.query(Customer).all()

    return show_customers_list(customers), 200

@app.get('/get_customer',
    tags=[customer_tag],
    responses={"200": CustomerViewSchema, "404": ErrorSchema}
)
def get_customer(query: CustomerKeySchema):
    """Get a customer by ID."""

    session = Session()

    customer_key = query.customer_key

    try:
        customer = session.query(Customer).filter(
            Customer.customer_key == customer_key).first()
        if customer is None:
            return {
                "message": "Customer not found"
            }, 404
    except NoResultFound:
        return {
            "message": "Customer not found"
        }, 404

    return show_customer_view(customer), 200


# ------------------------------------------------------------
# Travel Plan Routes
# ------------------------------------------------------------

@app.post('/add_travel_plan',
          tags=[travel_plan_tag],
          responses={"200": TravelPlanViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_travel_plan(form: TravelPlanSchema):
    """Add a new travel plan to the database."""

    session = Session()
    customer = session.query(Customer).filter(
        Customer.customer_key == form.customer_id
    ).first()

    if customer is None:
        return {"message": "Customer not found"}, 404

    travel_plan = TravelPlan(
        start_date=form.start_date,
        end_date=form.end_date,
        travel_purpose=form.travel_purpose,
        destination=form.destination,
        origin=form.origin,
        customer_id=form.customer_id,
    )

    session.add(travel_plan)
    session.flush()
    session.refresh(travel_plan)

    customer.travel_plan_id = travel_plan.travel_plan_key
    session.commit()

    return show_travel_plan_view(travel_plan), 200

@app.get('/get_travel_plan',
         tags=[travel_plan_tag],
         responses={"200": TravelPlanViewSchema, "404": ErrorSchema})
def get_travel_plan(query: TravelPlanKeySchema):
    """Retrieve a travel plan by key."""

    session = Session()
    travel_plan_key = query.travel_plan_key

    try:
        travel_plan = session.query(TravelPlan).filter(
            TravelPlan.travel_plan_key == travel_plan_key
        ).first()
        if travel_plan is None:
            return {"message": "Travel plan not found"}, 404
    except NoResultFound:
        return {"message": "Travel plan not found"}, 404

    return show_travel_plan_view(travel_plan), 200

if __name__ == "__main__":
    app.run(debug=True)
