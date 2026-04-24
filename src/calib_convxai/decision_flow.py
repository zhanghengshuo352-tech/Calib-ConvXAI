from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any, List


CALIBRATION_PROMPT = (
    "Before changing your answer, briefly state which two cues you relied on most."
)


@dataclass
class Task:
    task_id: str
    task_text: str
    ai_recommendation: str
    correct_answer: str


@dataclass
class TrialLog:
    participant_id: str
    condition: str
    task_id: str
    first_decision: str
    ai_recommendation: str
    disagreement_flag: bool
    calibration_prompt_triggered: bool
    calibration_prompt_response: Optional[str]
    final_decision: str
    final_correctness: bool
    switched_to_ai: bool
    retained_self_judgment: bool


class CalibConvXAIEngine:
    """
    Minimal prototype engine for the Calib-ConvXAI interaction logic.

    This class does not build a GUI yet.
    It only models the core behavioral logic of one task interaction.
    """

    def __init__(self, prompt_text: str = CALIBRATION_PROMPT) -> None:
        self.prompt_text = prompt_text

    def needs_calibration_prompt(self, first_decision: str, ai_recommendation: str) -> bool:
        return first_decision != ai_recommendation

    def run_trial(
        self,
        participant_id: str,
        condition: str,
        task: Task,
        first_decision: str,
        final_decision: str,
        calibration_prompt_response: Optional[str] = None,
    ) -> TrialLog:
        disagreement_flag = self.needs_calibration_prompt(
            first_decision=first_decision,
            ai_recommendation=task.ai_recommendation,
        )

        calibration_prompt_triggered = (
            condition.lower() == "calib-convxai" and disagreement_flag
        )

        if not calibration_prompt_triggered:
            calibration_prompt_response = None

        switched_to_ai = (
            disagreement_flag and final_decision == task.ai_recommendation
        )

        retained_self_judgment = final_decision == first_decision
        final_correctness = final_decision == task.correct_answer

        return TrialLog(
            participant_id=participant_id,
            condition=condition,
            task_id=task.task_id,
            first_decision=first_decision,
            ai_recommendation=task.ai_recommendation,
            disagreement_flag=disagreement_flag,
            calibration_prompt_triggered=calibration_prompt_triggered,
            calibration_prompt_response=calibration_prompt_response,
            final_decision=final_decision,
            final_correctness=final_correctness,
            switched_to_ai=switched_to_ai,
            retained_self_judgment=retained_self_judgment,
        )


def log_to_dict(log: TrialLog) -> Dict[str, Any]:
    return asdict(log)


def demo() -> List[Dict[str, Any]]:
    """
    Small demo showing one baseline trial and one Calib-ConvXAI trial.
    """
    task = Task(
        task_id="task_001",
        task_text="A user is shown a decision task with two possible labels: A or B.",
        ai_recommendation="B",
        correct_answer="A",
    )

    engine = CalibConvXAIEngine()

    baseline_log = engine.run_trial(
        participant_id="P001",
        condition="baseline-convxai",
        task=task,
        first_decision="A",
        final_decision="B",
        calibration_prompt_response=None,
    )

    calib_log = engine.run_trial(
        participant_id="P002",
        condition="calib-convxai",
        task=task,
        first_decision="A",
        final_decision="A",
        calibration_prompt_response="I relied on cue_1 and cue_2.",
    )

    return [log_to_dict(baseline_log), log_to_dict(calib_log)]


if __name__ == "__main__":
    logs = demo()
    print("=== Calib-ConvXAI Demo Logs ===")
    for i, log in enumerate(logs, start=1):
        print(f"\nTrial {i}")
        for key, value in log.items():
            print(f"{key}: {value}")