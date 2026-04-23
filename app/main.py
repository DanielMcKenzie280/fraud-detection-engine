from fastapi import FastAPI

from app.engine import evaluate_event
from app.models import FraudDetectionResult, FraudEvent

app = FastAPI(
    title="Fraud Detection Engine",
    description="Rule-based fraud detection API for suspicious transaction and player activity analysis.",
    version="1.1.0",
)


@app.get("/")
def root() -> dict:
    return {"message": "Fraud Detection Engine API is running"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post(
    "/detect",
    response_model=FraudDetectionResult,
    summary="Analyze player activity and detect fraud risk",
)
def detect_fraud(event: FraudEvent) -> FraudDetectionResult:
    return evaluate_event(event)
