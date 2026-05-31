import json
from pathlib import Path

from models.itinerary import (
    Activity,
    Accommodation,
    Flight,
    Itinerary,
    Transport,
    Traveler,
)


class ItineraryParser:

    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent.parent

    def load_json(self, filename: str):

        file_path = self.base_dir / "sample_data" / filename

        with open(file_path) as f:
            return json.load(f)

    def parse_itinerary(self, raw_trip: dict) -> Itinerary:

        traveler = Traveler(**raw_trip["traveler"])

        flights = [
            Flight(
                flight_number=f["flight_number"],
                from_=f["from"],
                to=f["to"],
                departure_time=f["departure_time"],
                arrival_time=f["arrival_time"],
            )
            for f in raw_trip.get("flights", [])
        ]

        accommodation = [
            Accommodation(**hotel)
            for hotel in raw_trip.get("accommodation", [])
        ]

        transport = [
            Transport(**t)
            for t in raw_trip.get("transport", [])
        ]

        activities = [
            Activity(**a)
            for a in raw_trip.get("activities", [])
        ]

        return Itinerary(
            trip_id=raw_trip["trip_id"],
            traveler=traveler,
            flights=flights,
            accommodation=accommodation,
            transport=transport,
            activities=activities,
        )

    def parse_all(self, filename="itineraries.json"):

        raw_data = self.load_json(filename)

        return [
            self.parse_itinerary(trip)
            for trip in raw_data
        ]