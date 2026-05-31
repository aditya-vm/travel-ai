from datetime import datetime
from typing import List

from pydantic import BaseModel


class Traveler(BaseModel):
    traveler_type: str
    pace: str
    budget: str
    interests: List[str]


class Flight(BaseModel):
    flight_number: str
    from_: str
    to: str
    departure_time: datetime
    arrival_time: datetime


class Accommodation(BaseModel):
    hotel_name: str
    city: str
    checkin: datetime
    checkout: datetime


class Transport(BaseModel):
    type: str
    pickup: str
    destination: str
    time: datetime


class Activity(BaseModel):
    day: int
    name: str
    time: str


class Itinerary(BaseModel):
    trip_id: str
    traveler: Traveler
    flights: List[Flight]
    accommodation: List[Accommodation]
    transport: List[Transport]
    activities: List[Activity]