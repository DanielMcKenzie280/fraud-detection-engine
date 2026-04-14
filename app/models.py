from typing import List
from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    user_id: str = Field(..., description="Unique user identifier")
    deposits: List[float] = Field(default_factory=list, description="List of deposit amounts")
    withdrawals: List[float] = Field(default_factory=list, description="List of withdrawal amounts")
    bonus_claimed: bool = Field(False, description="Whether the user claimed a bonus")
    session_minutes: int = Field(0, ge=0, description="Total session duration in minutes")
    bets_count: int = Field(0, ge=0, description="Number of bets placed")
    failed_payments: int = Field(0, ge=0, description="Number of failed payment attempts")
    account_age_days: int = Field(0, ge=0, description="Age of the account in days")


class AnalysisResponse(BaseModel):
    user_id: str
    risk_score: int
    risk_level: str
    flags: List[str]
