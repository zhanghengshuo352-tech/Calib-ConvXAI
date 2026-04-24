from __future__ import annotations

from typing import List, Dict, Any

from src.calib_convxai.decision_flow import Task, CalibConvXAIEngine, log_to_dict


def build_sample_tasks() -> List[Task]:
    return [
        Task(
            task_id="task_001",
            task_text="A user is shown a decision task with two possible labels: A or B.",
            ai_recommendation="B",
            correct_answer="A",
        ),
        Task(
            task_id="task_002",
            task_text="A second decision task with two possible labels: A or B.",
            ai_recommendation="B",
            correct_answer="A",
        ),
    ]


def build_sample_logs() -> List[Dict[str, Any]]:
    tasks = build_sample_tasks()
    engine = CalibConvXAIEngine()

    baseline_log = engine.run_trial(
        participant_id="P001",
        condition="baseline-convxai",
        task=tasks[0],
        first_decision="A",
        final_decision="B",
        calibration_prompt_response=None,
    )

    calib_log = engine.run_trial(
        participant_id="P002",
        condition="calib-convxai",
        task=tasks[1],
        first_decision="A",
        final_decision="A",
        calibration_prompt_response="I relied on cue_1 and cue_2.",
    )

    return [log_to_dict(baseline_log), log_to_dict(calib_log)]


if __name__ == "__main__":
    logs = build_sample_logs()
    print("=== Sample Logs Preview ===")
    for i, log in enumerate(logs, start=1):
        print(f"\nTrial {i}")
        for key, value in log.items():
            print(f"{key}: {value}")