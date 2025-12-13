from pydantic import BaseModel
from typing import Optional
from datetime import date

from database_model import TravelPlan


class TravelPlanKeySchema(BaseModel):
    """Defines how a TravelPlan key should be represented"""
    travel_plan_key: int


class TravelPlanSchema(BaseModel):
    """Defines how a new TravelPlan should be represented"""
    # Keep types aligned with your SQL entity (INT fields).
    # If you later switch to Date in the DB, change these to `date`.
    start_date: date
    end_date: date
    travel_purpose: str
    destination: str
    origin: str


class TravelPlanViewSchema(BaseModel):
    """Defines how a TravelPlan should be returned"""
    start_date = date
    end_date = date
    travel_purpose = str
    destination = str
    origin = str
    travel_plan_key = int


def show_travel_plan_view(travel_plan: TravelPlan):
    """Returns a travel plan view representation"""
    return {
        "start_date": travel_plan.start_date.isoformat(),
        "end_date": travel_plan.end_date.isoformat(),
        "travel_purpose": travel_plan.travel_purpose,
        "destination": travel_plan.destination,
        "origin": travel_plan.origin,
        "travel_plan_key": travel_plan.travel_plan_key,
    }
