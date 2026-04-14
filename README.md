# fraud-detection-engine

Rule-based fraud detection engine for online platforms. This project helps identify suspicious transaction behavior, bonus abuse patterns, and unusual player activity using configurable detection rules.

## Features

- Detects suspicious deposit and withdrawal patterns
- Flags bonus abuse indicators
- Identifies session-based risky behavior
- Supports configurable fraud rules
- REST API with FastAPI
- Ready for future ML scoring integration

## Use Cases

- Online casino and iGaming fraud monitoring
- Payment anomaly detection
- Bonus abuse prevention
- Session risk scoring
- Behavioral pattern analysis

## Example Detection Rules

- Multiple large deposits in a short period
- Rapid deposit-loss-deposit behavior
- Repeated bonus claims from related accounts
- Unusual session duration spikes
- High-frequency betting anomalies

## Tech Stack

- Python
- FastAPI
- Pydantic
- Rule-based scoring logic

## Project Structure

```bash
fraud-detection-engine/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── rules.py
│   ├── engine.py
│   └── utils.py
│
├── data/
│   └── sample_events.json
│
├── tests/
│   └── test_engine.py
│
├── requirements.txt
├── README.md
└── .gitignore
