from flask import Flask
from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag

from database_model.Customer import Customer
from database_model import Session

from schemas.Customer import CustomerViewSchema, CustomerSchema, show_customer_view
from schemas.error import ErrorSchema


info = Info(title="Bora Orneles Customer Area API", version="1.0.0")
app = OpenAPI(__name__, info=info)

customer_tag = Tag(name="Customer", description="Add customer to database")

@app.route("/")
def home():
     return redirect('/openapi')

@app.post('/customer',
          tags=[customer_tag],
          responses={"200": CustomerViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_customer(form: CustomerSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    customer = Customer(
        full_name=form.full_name,
        date_of_birth=form.date_of_birth,
        e_mail=form.e_mail,
        home_adress=form.home_adress
        )

    # criando conexão com a base
    session = Session()
    # adicionando produto
    session.add(customer)
    # efetivando o camando de adição de novo item na tabela
    session.commit()
    return show_customer_view(customer), 200

if __name__ == "__main__":
    app.run(debug=True)