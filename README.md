# Travel Itinerary Optimization and Summary Generator

An AI-powered travel assistant that transforms complex travel itineraries into clear, personalized, and easy-to-understand travel summaries.

The system parses structured travel data (JSON), detects risks and optimization opportunities (tight layovers, fatigue, hotel timing issues), and generates traveler-friendly summaries using an LLM.

---

## Problem Statement

Travel itineraries often contain:

- Multiple flights and transport modes
- Hotel bookings and check-in constraints
- Activities spread across days
- Tight layovers and travel risks

These can be difficult for travelers to understand quickly.

This project solves that by:

1. Parsing structured itinerary data
2. Optimizing travel insights using deterministic logic
3. Generating concise, personalized summaries using an LLM

---

## Features

### Itinerary Parsing
- Parses travel itinerary JSON files
- Converts raw input into structured object models
- Supports:
  - Flights
  - Hotels / accommodation
  - Transport
  - Activities
  - Traveler preferences

### Travel Optimization
Detects:

- Tight layovers
- High-risk connections
- Overnight flights
- Long hotel check-in wait times
- Travel fatigue level
- Personalized travel recommendations

### AI Summarization
Generates:

- Day-wise itinerary summaries
- Flight and hotel explanations
- Activity schedules
- Travel warnings and recommendations
- Personalized travel tips

---

## Architecture

```text
Raw JSON / CSV
        ↓
Parser
        ↓
Normalized Itinerary Object
        ↓
Travel Optimizer
        ↓
Travel Insights
        ↓
LLM Summarizer
        ↓
Human-Friendly Travel Summary
```

---

## Tech Stack

### Backend
- Python 3.10+

### Libraries
- Pydantic (schema validation)
- OpenAI SDK
- python-dotenv

### LLM Provider
- OpenRouter API

---

## Project Structure

```text
travel-ai/
│
├── main.py
│
├── models/
│   ├── itinerary.py
│   └── optimization.py
│
├── services/
│   ├── parser.py
│   ├── optimizer.py
│   ├── summarizer.py
│   └── llm.py
│
├── sample_data/
│   └── itineraries.json
│
├── .env
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone repository

```bash
git clone <repo-url>
cd travel-ai
```

---

### 2. Create virtual environment

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure API key

Create a `.env` file in the root directory.

Example:

```text
OPENROUTER_API_KEY=your_api_key_here
```

Get your API key from:

https://openrouter.ai/settings/keys

---

## Input Data Format

Example itinerary:

```json
{
  "trip_id": "TRIP001",

  "traveler": {
    "traveler_type": "solo",
    "pace": "relaxed",
    "budget": "medium",
    "interests": [
      "food",
      "culture"
    ]
  },

  "flights": [
    {
      "flight_number": "AI245",
      "from": "Hyderabad",
      "to": "Dubai",
      "departure_time": "2026-08-10T02:10:00",
      "arrival_time": "2026-08-10T05:50:00"
    }
  ],

  "accommodation": [
    {
      "hotel_name": "Paris Central Hotel",
      "city": "Paris",
      "checkin": "2026-08-10T16:00:00",
      "checkout": "2026-08-14T11:00:00"
    }
  ],

  "transport": [
    {
      "type": "metro",
      "pickup": "CDG Airport",
      "destination": "Paris Central Hotel",
      "time": "2026-08-10T12:00:00"
    }
  ],

  "activities": [
    {
      "day": 2,
      "name": "Louvre Museum",
      "time": "10:00"
    }
  ]
}
```

---

## How It Works

### 1. Parser

Converts raw itinerary JSON into validated object models.

Input:

```text
JSON
```

Output:

```python
Itinerary object
```

---

### 2. Optimizer

Analyzes itinerary for travel risks and recommendations.

Example outputs:

```python
{
  "warnings": [
    "Tight connection at Dubai"
  ],

  "tips": [
    "Overnight flight detected"
  ],

  "travel_stress_score": 5,
  "fatigue_level": "medium"
}
```

---

### 3. Summarizer (LLM Layer)

Combines:

- itinerary facts
- optimizer insights
- traveler preferences

to generate:

```text
Day 1:
Depart Hyderabad at 2:10 AM and transit via Dubai.

You have a tight layover, so proceed quickly between gates.

Arrive in Paris and travel to your hotel via metro.

Since check-in begins later in the day, consider relaxing nearby.

Day 2:
Visit Louvre Museum at 10:00 AM.
```

---

## Run the Project

```bash
python main.py
```

---

## Example Flow

```text
itineraries.json
        ↓
Parser
        ↓
Structured itinerary
        ↓
Optimizer
        ↓
Warnings + Tips
        ↓
LLM Summarizer
        ↓
Readable travel summary
```

---

## Example Use Cases

### Solo Traveler
- Safety reminders
- Budget transport suggestions
- Fatigue reduction tips

### Family Traveler
- Relaxed pacing
- Extra transfer buffer warnings
- Child-friendly recommendations

### Business Traveler
- Fastest transport suggestions
- Efficient schedules
- Meeting-friendly summaries

---

## Design Philosophy

This system intentionally separates:

### Deterministic reasoning
(Python optimizer)

from

### Natural language generation
(LLM summarizer)

This improves:

- Reliability
- Explainability
- Maintainability
- LLM output quality

Instead of asking the LLM to infer everything from raw JSON, the optimizer computes structured travel insights first and the LLM converts them into user-friendly summaries.

---

## License

MIT