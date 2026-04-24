from __future__ import annotations

from typing import Any, Dict, Mapping, Sequence, Union

from src.calib_convxai.decision_flow import demo

LogLike = Union[Mapping[str, Any], Dict[str, Any]]


def get_field(log: LogLike, field: str) -> Any:
    return log[field]


def total_trials(logs: Sequence[LogLike]) -> int:
    return len(logs)


def disagreement_rate(logs: Sequence[LogLike]) -> float:
    if not logs:
        return 0.0
    disagreements = sum(bool(get_field(log, "disagreement_flag")) for log in logs)
    return disagreements / len(logs)


def calibration_trigger_rate(logs: Sequence[LogLike]) -> float:
    if not logs:
        return 0.0
    triggered = sum(bool(get_field(log, "calibration_prompt_triggered")) for log in logs)
    return triggered / len(logs)


def agreement_fraction(logs: Sequence[LogLike]) -> float:
    if not logs:
        return 0.0
    agreements = sum(
        get_field(log, "final_decision") == get_field(log, "ai_recommendation")
        for log in logs
    )
    return agreements / len(logs)


def switch_fraction(logs: Sequence[LogLike]) -> float:
    disagreement_logs = [log for log in logs if bool(get_field(log, "disagreement_flag"))]
    if not disagreement_logs:
        return 0.0
    switched = sum(bool(get_field(log, "switched_to_ai")) for log in disagreement_logs)
    return switched / len(disagreement_logs)


def final_accuracy(logs: Sequence[LogLike]) -> float:
    if not logs:
        return 0.0
    correct = sum(bool(get_field(log, "final_correctness")) for log in logs)
    return correct / len(logs)


def summarize_logs(logs: Sequence[LogLike]) -> Dict[str, float]:
    return {
        "total_trials": float(total_trials(logs)),
        "disagreement_rate": disagreement_rate(logs),
        "calibration_trigger_rate": calibration_trigger_rate(logs),
        "agreement_fraction": agreement_fraction(logs),
        "switch_fraction": switch_fraction(logs),
        "final_accuracy": final_accuracy(logs),
    }


def print_summary(summary: Dict[str, float]) -> None:
    print("=== Metrics Summary ===")
    for key, value in summary.items():
        if key == "total_trials":
            print(f"{key}: {int(value)}")
        else:
            print(f"{key}: {value:.3f}")


def main() -> None:
    logs = demo()
    summary = summarize_logs(logs)
    print_summary(summary)


if __name__ == "__main__":
    main()