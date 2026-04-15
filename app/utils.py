def calculate_risk_level(score: int) -> str:
    if score >= 75:
        return "critical"
    if score >= 50:
        return "high"
    if score >= 25:
        return "medium"
    return "low"


def build_recommendation(risk_level: str) -> str:
    mapping = {
        "low": "no immediate action required",
        "medium": "monitor account activity",
        "high": "manual review suggested",
        "critical": "manual fraud review required",
    }
    return mapping[risk_level]
