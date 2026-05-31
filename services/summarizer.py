from models.itinerary import Itinerary
from models.optimization import OptimizationResult
from services.llm import LLMClient


class TravelSummarizer:

    def __init__(self):
        self.llm = LLMClient()

    def summarize(self,itinerary: Itinerary,optimization: OptimizationResult):

        prompt = f"""
                    You are an AI travel concierge.

                    Generate a concise and friendly
                    travel itinerary summary.

                    Rules:
                    - Organize day-wise
                    - Mention flights
                    - Mention hotel check-in
                    - Mention transport
                    - Mention activities
                    - Mention travel warnings
                    - Mention travel tips
                    - Personalize based on traveler type
                    - Keep language easy to understand
                    - Keep it concise

                    Traveler profile:
                    {itinerary.traveler.model_dump()}

                    Flights:
                    {[f.model_dump() for f in itinerary.flights]}

                    Accommodation:
                    {[a.model_dump()for a in itinerary.accommodation]}

                    Transport:
                    {[t.model_dump()for t in itinerary.transport]}

                    Activities:
                    {[a.model_dump()for a in itinerary.activities]}

                    Travel analysis:
                    {optimization.model_dump()}

                    Generate summary.
                    """

        return self.llm.generate(prompt)