"""Utility to add a predefined set of customers to the database."""

from datetime import date
from pathlib import Path
import sys

# Ensure project root is on sys.path so database_model can be imported.
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from database_model import Session
from database_model.Customer import Customer


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


def seed_customers():
    """Create static customers inside a single transaction."""
    session = Session()
    try:
        for data in CUSTOMERS_DATA:
            session.add(Customer(**data))
        session.commit()
        print(f"Inserted {len(CUSTOMERS_DATA)} customers.")
    except Exception as exc:
        session.rollback()
        raise RuntimeError("Failed to seed customers") from exc
    finally:
        session.close()


if __name__ == "__main__":
    seed_customers()
