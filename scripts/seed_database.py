"""Utility to seed travel plans and customers into the local database."""

from datetime import date
from pathlib import Path
import sys

# Ensure project root is on sys.path so database_model can be imported.
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from database_model import Session  # noqa: E402
from database_model.Customer import Customer  # noqa: E402
from database_model.TravelPlan import TravelPlan  # noqa: E402


TRAVEL_PLANS = [
    {
        "start_date": date(2025, 2, 26),
        "end_date": date(2025, 3, 5),
        "travel_purpose": "Carnaval vacation",
        "destination": "Rio de Janeiro",
        "origin": "Sao Paulo",
        "target_customer_index": 1,
    },
    {
        "start_date": date(2025, 1, 15),
        "end_date": date(2025, 1, 25),
        "travel_purpose": "Beach retreat",
        "destination": "Florianopolis",
        "origin": "Curitiba",
        "target_customer_index": 3,
    },
    {
        "start_date": date(2025, 7, 10),
        "end_date": date(2025, 7, 18),
        "travel_purpose": "Festival visit",
        "destination": "Salvador",
        "origin": "Recife",
        "target_customer_index": 5,
    },
    {
        "start_date": date(2025, 5, 5),
        "end_date": date(2025, 5, 15),
        "travel_purpose": "Eco tour",
        "destination": "Manaus",
        "origin": "Belem",
        "target_customer_index": 7,
    },
    {
        "start_date": date(2025, 9, 2),
        "end_date": date(2025, 9, 6),
        "travel_purpose": "Business meetings",
        "destination": "Porto Alegre",
        "origin": "Brasilia",
        "target_customer_index": 9,
    },
]


CUSTOMERS_DATA = [
    {
        "full_name": "Ana Beatriz Souza",
        "date_of_birth": date(1990, 5, 14),
        "e_mail": "ana.souza@example.com",
        "home_adress": "Rua das Mangueiras, 123",
        "social_number": "SN-0001",
        "travel_plan_id": None,
    },
    {
        "full_name": "Bruno Machado",
        "date_of_birth": date(1985, 8, 22),
        "e_mail": "bruno.machado@example.com",
        "home_adress": "Avenida Brasil, 456",
        "social_number": "SN-0002",
        "travel_plan_id": None,
    },
    {
        "full_name": "Carla Menezes",
        "date_of_birth": date(1992, 1, 5),
        "e_mail": "carla.menezes@example.com",
        "home_adress": "Rua Ipe Roxo, 789",
        "social_number": "SN-0003",
        "travel_plan_id": None,
    },
    {
        "full_name": "Daniel Oliveira",
        "date_of_birth": date(1988, 3, 19),
        "e_mail": "daniel.oliveira@example.com",
        "home_adress": "Rua das Palmeiras, 321",
        "social_number": "SN-0004",
        "travel_plan_id": None,
    },
    {
        "full_name": "Eduarda Campos",
        "date_of_birth": date(1995, 11, 30),
        "e_mail": "eduarda.campos@example.com",
        "home_adress": "Rua das Flores, 654",
        "social_number": "SN-0005",
        "travel_plan_id": None,
    },
    {
        "full_name": "Felipe Araujo",
        "date_of_birth": date(1991, 4, 2),
        "e_mail": "felipe.araujo@example.com",
        "home_adress": "Rua do Sol, 987",
        "social_number": "SN-0006",
        "travel_plan_id": None,
    },
    {
        "full_name": "Gabriela Lima",
        "date_of_birth": date(1983, 7, 17),
        "e_mail": "gabriela.lima@example.com",
        "home_adress": "Rua da Paz, 258",
        "social_number": "SN-0007",
        "travel_plan_id": None,
    },
    {
        "full_name": "Henrique Borges",
        "date_of_birth": date(1994, 9, 9),
        "e_mail": "henrique.borges@example.com",
        "home_adress": "Rua das Laranjeiras, 369",
        "social_number": "SN-0008",
        "travel_plan_id": None,
    },
    {
        "full_name": "Isabela Nunes",
        "date_of_birth": date(1987, 2, 27),
        "e_mail": "isabela.nunes@example.com",
        "home_adress": "Avenida Atlantica, 147",
        "social_number": "SN-0009",
        "travel_plan_id": None,
    },
    {
        "full_name": "Joao Pedro Carvalho",
        "date_of_birth": date(1993, 12, 12),
        "e_mail": "joao.carvalho@example.com",
        "home_adress": "Rua Santa Clara, 753",
        "social_number": "SN-0010",
        "travel_plan_id": None,
    },
]


def seed_database():
    """Create travel plans and customers inside a single transaction."""
    session = Session()
    try:
        customers = {}
        for idx, data in enumerate(CUSTOMERS_DATA, start=1):
            payload = data.copy()
            customer = Customer(**payload)
            session.add(customer)
            session.flush()
            customers[idx] = customer.customer_key

        travel_plan_entries = []
        for plan in TRAVEL_PLANS:
            target_index = plan["target_customer_index"]
            customer_key = customers.get(target_index)
            if not customer_key:
                raise ValueError(
                    f"No customer seeded for travel plan target index {target_index}"
                )
            travel_plan = TravelPlan(
                start_date=plan["start_date"],
                end_date=plan["end_date"],
                travel_purpose=plan["travel_purpose"],
                destination=plan["destination"],
                origin=plan["origin"],
                customer_id=customer_key,
            )
            session.add(travel_plan)
            session.flush()
            travel_plan_entries.append((customer_key, travel_plan.travel_plan_key))

        for customer_key, travel_plan_key in travel_plan_entries:
            session.query(Customer).filter(
                Customer.customer_key == customer_key
            ).update({"travel_plan_id": travel_plan_key})

        session.commit()
        print(
            f"Inserted {len(travel_plan_entries)} travel plans and "

            f"{len(CUSTOMERS_DATA)} customers."
        )
    except Exception as exc:
        session.rollback()
        raise RuntimeError("Failed to seed travel plans and customers") from exc
    finally:
        session.close()


if __name__ == "__main__":
    seed_database()
