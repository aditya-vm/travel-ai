from services.parser import ItineraryParser
from services.optimizer import TravelOptimizer
from services.summarizer import TravelSummarizer

parser = ItineraryParser()
optimizer = TravelOptimizer()
summarizer = TravelSummarizer()


trips = parser.parse_all()
trip = trips[0]

optimizations = optimizer.optimize(trip)

# print(optimizations.model_dump())

summary = summarizer.summarize(trip, optimizations)

print(summary)