from __future__ import annotations

from src.calib_convxai.decision_flow import CalibConvXAIEngine
from src.calib_convxai.sample_data import build_sample_tasks


def normalize_answer(text: str) -> str:
    return text.strip().upper()


def choose_condition() -> str:
    print("Choose condition:")
    print("1. baseline-convxai")
    print("2. calib-convxai")
    choice = input("Enter 1 or 2 [default=2]: ").strip()

    if choice == "1":
        return "baseline-convxai"
    return "calib-convxai"


def ask_decision(prompt: str) -> str:
    while True:
        answer = normalize_answer(input(prompt))
        if answer in {"A", "B"}:
            return answer
        print("Please enter A or B.")


def main() -> None:
    print("=== Calib-ConvXAI CLI Demo ===\n")

    condition = choose_condition()
    task = build_sample_tasks()[0]
    engine = CalibConvXAIEngine()

    print("\nTask:")
    print(task.task_text)
    print("\nPossible labels: A / B")

    first_decision = ask_decision("\nEnter your first decision (A/B): ")

    disagreement = engine.needs_calibration_prompt(
        first_decision=first_decision,
        ai_recommendation=task.ai_recommendation,
    )

    calibration_prompt_response = None
    if condition == "calib-convxai" and disagreement:
        print("\nCalibration prompt triggered:")
        print(engine.prompt_text)
        calibration_prompt_response = input("Your response: ").strip()

    print("\nAI recommendation:")
    print(task.ai_recommendation)

    final_decision = ask_decision("\nEnter your final decision (A/B): ")

    log = engine.run_trial(
        participant_id="CLI_USER",
        condition=condition,
        task=task,
        first_decision=first_decision,
        final_decision=final_decision,
        calibration_prompt_response=calibration_prompt_response,
    )

    print("\n=== Trial Result ===")
    for key, value in log.__dict__.items():
        print(f"{key}: {value}")

    print("\n=== Quick Interpretation ===")
    if log.negative_ai_reliance_like:
        print("This looks like an overreliance-like case: the user followed incorrect AI advice.")
    elif log.positive_self_reliance_like:
        print("This looks like a positive self-reliance-like case: the user maintained a correct judgment.")
    elif log.positive_ai_reliance_like:
        print("This looks like a positive AI-reliance-like case: the user appropriately adopted correct AI advice.")
    elif log.negative_self_reliance_like:
        print("This looks like a negative self-reliance-like case: the user failed to adopt correct AI advice.")
    else:
        print("This trial does not strongly match one of the four reliance-like categories.")


if __name__ == "__main__":
    main()