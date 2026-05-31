from datetime import timedelta

from models.itinerary import Itinerary
from models.optimization import OptimizationResult


class TravelOptimizer:

    def optimize(
        self,
        itinerary: Itinerary
    ) -> OptimizationResult:

        warnings = []
        tips = []
        layover_analysis = []

        stress_score = 1

        
        # 1. Analyze layovers
        
        flights = itinerary.flights

        for i in range(len(flights) - 1):

            current_flight = flights[i]
            next_flight = flights[i + 1]

            layover = (
                next_flight.departure_time
                -
                current_flight.arrival_time
            )

            layover_hours = layover.total_seconds() / 3600

            message = (
                f"{current_flight.to} layover: "
                f"{round(layover_hours,1)} hours"
            )

            layover_analysis.append(message)

            if layover_hours < 1:

                warnings.append(
                    f"High risk connection at "
                    f"{current_flight.to}: "
                    f"only {round(layover_hours,1)} "
                    f"hour layover"
                )

                stress_score += 3

            elif layover_hours < 2:

                warnings.append(
                    f"Tight connection at "
                    f"{current_flight.to}"
                )

                stress_score += 2

            elif layover_hours > 6:

                tips.append(
                    f"Long layover at "
                    f"{current_flight.to}. "
                    f"Consider airport lounge "
                    f"or nearby exploration."
                )

        
        # 2. Overnight flight
        
        for flight in flights:

            departure_hour = (
                flight.departure_time.hour
            )

            arrival_hour = (
                flight.arrival_time.hour
            )

            if (
                departure_hour >= 22
                or
                arrival_hour <= 6
            ):

                tips.append(
                    "Overnight flight detected. "
                    "Consider rest after arrival."
                )

                stress_score += 1

        
        # 3. Hotel check-in wait
        

        if (
            itinerary.accommodation
            and flights
        ):

            hotel = itinerary.accommodation[0]

            final_arrival = (
                flights[-1].arrival_time
            )

            wait_time = (
                hotel.checkin
                -
                final_arrival
            )

            wait_hours = (
                wait_time.total_seconds()
                /
                3600
            )

            if wait_hours > 4:

                tips.append(
                    f"{round(wait_hours,1)} hour "
                    f"wait before hotel check-in."
                )

                stress_score += 1

        
        # 4. Personalization

        traveler_type = (
            itinerary.traveler
            .traveler_type
        )

        if traveler_type == "family":

            tips.append(
                "Family trip detected. "
                "Allow extra transfer time."
            )

        elif traveler_type == "business":

            tips.append(
                "Business traveler: "
                "prioritize efficient transport."
            )

        elif traveler_type == "solo":

            tips.append(
                "Solo traveler: "
                "keep emergency contacts handy."
            )

        
        # 5. Fatigue level
        

        if stress_score <= 3:
            fatigue_level = "low"

        elif stress_score <= 6:
            fatigue_level = "medium"

        else:
            fatigue_level = "high"

        stress_score = min(
            stress_score,
            10
        )

        return OptimizationResult(
            warnings=warnings,
            tips=tips,
            layover_analysis=layover_analysis,
            travel_stress_score=stress_score,
            fatigue_level=fatigue_level
        )