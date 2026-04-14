from app.models import AnalysisRequest


def check_high_deposit_frequency(data: AnalysisRequest) -> tuple[int, str | None]:
    if len(data.deposits) >= 3:
        return 20, "high_deposit_frequency"
    return 0, None


def check_large_total_deposits(data: AnalysisRequest) -> tuple[int, str | None]:
    if sum(data.deposits) >= 1000:
        return 15, "large_total_deposits"
    return 0, None


def check_bonus_abuse_pattern(data: AnalysisRequest) -> tuple[int, str | None]:
    if data.bonus_claimed and len(data.deposits) >= 2 and data.account_age_days <= 7:
        return 25, "bonus_abuse_pattern"
    return 0, None


def check_extended_session(data: AnalysisRequest) -> tuple[int, str | None]:
    if data.session_minutes >= 300:
        return 15, "extended_session_duration"
    return 0, None


def check_high_betting_activity(data: AnalysisRequest) -> tuple[int, str | None]:
    if data.bets_count >= 500:
        return 10, "high_betting_activity"
    return 0, None


def check_failed_payments(data: AnalysisRequest) -> tuple[int, str | None]:
    if data.failed_payments >= 3:
        return 20, "multiple_failed_payments"
    return 0, None


def check_withdrawal_after_bonus(data: AnalysisRequest) -> tuple[int, str | None]:
    if data.bonus_claimed and len(data.withdrawals) > 0 and sum(data.withdrawals) > 0:
        return 10, "withdrawal_after_bonus"
    return 0, None


def get_all_rules():
    return [
        check_high_deposit_frequency,
        check_large_total_deposits,
        check_bonus_abuse_pattern,
        check_extended_session,
        check_high_betting_activity,
        check_failed_payments,
        check_withdrawal_after_bonus,
    ]
