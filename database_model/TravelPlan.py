from sqlalchemy import Column, Integer, Date, String
from datetime import date
from typing import Optional

from database_model.base import Base


class TravelPlan(Base):
    __tablename__ = "travel_plan"

    travel_plan_key = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, default=date.min)
    end_date = Column(Date, default=date.min)

    travel_purpose = Column(String)
    destination = Column(String)
    origin = Column(String)

    def __init__(
        self,
        start_date: date,
        end_date: date,
        travel_purpose: str,
        destination: str,
        origin: str,
        travel_plan_key: Optional[int] = None,
    ):
        self.start_date = start_date
        self.end_date = end_date
        self.travel_purpose = travel_purpose
        self.destination = destination
        self.origin = origin
        if travel_plan_key is not None:
            self.travel_plan_key = travel_plan_key
