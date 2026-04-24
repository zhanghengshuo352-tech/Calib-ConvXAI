# Interface Logic

## 1. Purpose

The purpose of this document is to specify the interaction logic of **Calib-ConvXAI**.

This project does not aim to build a more persuasive conversational assistant.  
Instead, it aims to build a **better-calibrated human-AI decision interaction**.

The design logic is based on two insights:

1. The ConvXAI baseline shows that conversational explanations can improve user understanding and trust, but may also increase overreliance.  
2. Cognitive forcing research shows that lightweight reflective friction can reduce overreliance, although there may be some trade-off in subjective experience.

---

## 2. Core Interaction Principle

The interaction principle of Calib-ConvXAI is:

**Only intervene when the user is at a meaningful risk of inappropriate reliance.**

In the first version of the system, “meaningful risk” is operationalized as:

**user first decision ≠ AI recommendation**

This means the calibration layer is not always active.  
It appears only when disagreement occurs.

This design keeps the system lightweight and focuses the intervention on the cases where switching, appropriate reliance, and overreliance are most relevant.

---

## 3. Baseline ConvXAI Logic

### Baseline flow

1. Show task to user  
2. User makes **first decision**  
3. Show AI recommendation  
4. Show conversational explanation  
5. User makes **final decision**  
6. Store task-level decision records

### Interpretation

This baseline logic allows the system to compare:

- what the user thought before seeing AI,
- what the AI recommended,
- and whether the user changed after seeing the explanation.

This is the basic structure needed to evaluate reliance behavior.

---

## 4. Calib-ConvXAI Logic

### Calibration-aware flow

1. Show task to user  
2. User makes **first decision**  
3. System compares first decision with AI recommendation  
4. If there is **no disagreement**, continue normally  
5. If there **is disagreement**, trigger calibration prompt  
6. User completes short reflection prompt  
7. Show AI recommendation  
8. Show conversational explanation  
9. User makes **final decision**  
10. Store task-level decision records, including calibration response

### Key difference from baseline

The baseline presents the explanation directly after the first decision.  
Calib-ConvXAI inserts a **short reflective checkpoint** before the explanation is consumed in disagreement cases.

The purpose is not to block AI use, but to create a brief moment of analytic engagement before users revise their answers.

---

## 5. Trigger Logic

### Trigger condition

The calibration prompt is shown only if:

**first_decision != ai_recommendation**

### Why this trigger is used

This trigger is chosen for three reasons:

1. It matches the most meaningful cases for reliance analysis.  
2. It avoids adding friction to every interaction.  
3. It keeps the first prototype simple and experimentally interpretable.

The ConvXAI baseline emphasizes that reliance quality should not be reduced to general trust or agreement alone, and disagreement cases are especially important for understanding switching and appropriate reliance.

---

## 6. Calibration Prompt Design

### Selected first prompt

**Before changing your answer, briefly state which two cues you relied on most.**

### Why this version is selected

This version is selected because it is:

- short,
- neutral in tone,
- easy to implement,
- and easy to analyze.

It also avoids sounding accusatory or overly instructional.  
The system is not telling the user “you may be wrong.”  
It is only encouraging the user to inspect their own reasoning before changing their answer.

### What the prompt is expected to do

The prompt is expected to:

- reduce impulsive switching,
- encourage explicit self-reflection,
- and make answer revision more deliberate.

This is conceptually similar to cognitive forcing, but adapted into a conversation-compatible micro-intervention.

---

## 7. Minimal UI Components

The first prototype does not need a full chatbot implementation.

It only needs the following UI elements:

### Task area
- task content
- task ID

### First decision area
- user selects initial answer

### Calibration prompt area
- appears only in disagreement cases
- includes one short text box or short response field

### AI response area
- AI recommendation
- explanation text

### Final decision area
- user confirms or revises answer

### Logging layer
- records all key actions and outputs

This keeps the prototype feasible while still preserving the core behavioral logic of the study.

---

## 8. Data Fields to Record

For each task interaction, the system should record:

- participant_id
- condition
- task_id
- first_decision
- ai_recommendation
- disagreement_flag
- calibration_prompt_triggered
- calibration_prompt_response
- final_decision
- final_correctness
- switched_to_ai
- retained_self_judgment
- optional confidence
- optional time_spent

These fields will later support the computation of reliance-related measures such as switching behavior and self-reliance patterns.

---

## 9. Design Constraints

The first version of Calib-ConvXAI should follow these constraints:

### Constraint 1
Do not add multiple interventions at once.

Only one calibration prompt should be used in version 1.

### Constraint 2
Do not build unnecessary product complexity.

The goal is a research prototype, not a polished commercial assistant.

### Constraint 3
Do not over-optimize the wording too early.

The purpose of the pilot is to test the mechanism, not to perfect every sentence.

### Constraint 4
Preserve comparability with baseline ConvXAI.

The intervention should be the main change, so that later comparisons remain interpretable.

---

## 10. Main Design Claim

The main design claim of this interface is:

**A short, disagreement-triggered calibration prompt may reduce overreliance by making users reflect before changing their answer, while preserving the useful parts of conversational explanation.**

This claim is grounded in:
- the ConvXAI finding that explanation quality does not automatically yield calibrated reliance, and
- the cognitive forcing finding that reflective friction can reduce overreliance.

---

## 11. Future Extension Possibilities

After the first prototype, the design can later be extended in several ways:

- compare multiple prompt styles
- add confidence-aware triggers
- compare disagreement-only vs always-on prompting
- integrate uncertainty presentation
- compare dashboard, ConvXAI, and Calib-ConvXAI together

These are future directions, not part of the first implementation.

For version 1, the design should remain minimal and focused.

---

## 12. Current Design Philosophy

Calib-ConvXAI is not designed to make users agree with AI more often.

It is designed to make users agree with AI **more appropriately**.

That means:
- less blind switching,
- more deliberate revision,
- and better-calibrated human-AI decision making.