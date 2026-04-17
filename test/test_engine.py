from app.engine import evaluate_event
from app.models import FraudEvent


def test_evaluate_event_returns_expected_result() -> None:
    event = FraudEvent(
        player_id="player_1001",
        session_id="session_9001",
        deposits=[200, 250, 300],
        withdrawals=[20, 25],
        bonus_claimed=True,
        related_accounts_count=3,
        session_duration_minutes=185,
        average_bet=5,
        max_bet=90,
        net_loss=420,
    )

    result = evaluate_event(event)

    assert result.player_id == "player_1001"
    assert result.session_id == "session_9001"
    assert result.risk_score > 0
    assert result.risk_level in {"medium", "high", "critical"}
    assert len(result.flags) > 0
