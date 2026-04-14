from fastapi import FastAPI
from app.models import AnalysisRequest, AnalysisResponse
from app.engine import analyze_user_risk

app = FastAPI(
    title="Fraud Detection Engine",
    version="1.0.0",
    description="Rule-based fraud detection engine for online platforms."
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Fraud Detection Engine API is running"}


@app.post("/analyze", response_model=AnalysisResponse)
def analyze(request: AnalysisRequest) -> AnalysisResponse:
    return analyze_user_risk(request)
