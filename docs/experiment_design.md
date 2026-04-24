# Experiment Design

## 1. Objective

The goal of this study is to test whether a **calibration-aware conversational XAI** can reduce overreliance in human-AI decision making.

More specifically, this project asks whether adding a lightweight reflective prompt at the moment of **user–AI disagreement** can improve reliance calibration, especially when the AI recommendation is wrong. This direction is directly motivated by the ConvXAI baseline, which shows that conversational explanations can improve understanding and trust but may also increase overreliance.

---

## 2. Experimental Conditions

### Condition A: Baseline ConvXAI
Participants interact with a standard conversational XAI interface.

Flow:
1. View task
2. Make first decision
3. View AI recommendation and conversational explanation
4. Make final decision

### Condition B: Calib-ConvXAI
Participants interact with a calibration-aware conversational XAI interface.

Flow:
1. View task
2. Make first decision
3. System checks whether first decision disagrees with AI recommendation
4. If disagreement occurs, show a calibration prompt
5. View AI recommendation and conversational explanation
6. Make final decision

This design keeps the baseline interaction structure intact while introducing one targeted intervention layer.

---

## 3. Trigger Rule

The calibration prompt is triggered only when:

**first decision ≠ AI recommendation**

This trigger rule is chosen because disagreement cases are the most informative for evaluating reliance quality. In the ConvXAI framework, measures such as switching and relative reliance are meaningful precisely when the user and AI initially disagree.

---

## 4. Calibration Prompt

### Selected Prompt
**Before changing your answer, briefly state which two cues you relied on most.**

### Rationale
This prompt is designed to:
- introduce a short reflective pause,
- encourage users to inspect their own reasoning,
- reduce impulsive switching toward AI,
- remain lightweight enough for a pilot study.

The design is inspired by the broader idea of cognitive forcing, where small reflective frictions can reduce overreliance in AI-assisted decision making.

---

## 5. Research Hypotheses

### H1
Compared with baseline ConvXAI, Calib-ConvXAI will improve **RSR**, meaning users will be better able to maintain correct self-reliance when the AI is wrong.

### H2
Compared with baseline ConvXAI, Calib-ConvXAI will reduce inappropriate switching while maintaining similar or only slightly reduced **RAIR**.

### H3
Calib-ConvXAI may slightly reduce subjective smoothness or convenience, but it will improve reliance calibration overall.

These hypotheses follow the core tension identified by the ConvXAI paper and the trade-off pattern observed in cognitive forcing research.

---

## 6. Measures

## Primary Measure

### RSR (Relative Positive Self-Reliance)
This is the main metric of the study.

Why:
- it captures whether users maintain their correct judgment when the AI is wrong,
- it is one of the clearest indicators of overreliance,
- and it directly reflects the main purpose of the intervention.

The ConvXAI baseline uses reliance-sensitive measures such as RAIR and RSR to distinguish appropriate reliance from mere agreement.

## Secondary Measures

### RAIR
Used to measure whether users appropriately adopt correct AI advice.

### Switch Fraction
Used to measure how often users switch toward AI after initial disagreement.

### Agreement Fraction
Used to measure how often users end up agreeing with AI overall.

## Supporting Measures

### Trust-related measures
Used to observe whether the calibration intervention reduces blind trust or changes user trust patterns.

### Explanation usefulness
Used to examine whether the intervention affects perceived explanation utility.

### Objective feature understanding
Used to check whether calibration support harms or preserves understanding.

---

## 7. Data to Record

For each participant and each task, the system should record:

- participant ID
- condition
- task ID
- first decision
- AI recommendation
- whether disagreement occurred
- whether calibration prompt was triggered
- calibration prompt response
- final decision
- correctness of final decision
- switching behavior
- confidence (if available)
- time spent (if available)

These fields are sufficient to compute reliance-related metrics and compare the two conditions.

---

## 8. Pilot Study Scope

This first study is intentionally small.

### Why only 2 conditions?
Because the main goal of the pilot is not to exhaustively compare many interfaces, but to test one focused intervention against the baseline.

This helps:
- reduce implementation burden,
- simplify interpretation,
- and make the first result easier to analyze.

If the pilot shows promising calibration effects, the design can later be expanded to include dashboard-based or other conversational variants.

---

## 9. Analysis Plan

The analysis will proceed in three stages:

### Stage 1: Descriptive Statistics
Summarize the distribution of:
- RSR
- RAIR
- switch fraction
- agreement fraction
- trust and understanding measures

### Stage 2: Condition Comparison
Compare Baseline ConvXAI and Calib-ConvXAI on the main measures.

If assumptions for parametric tests are not satisfied, non-parametric comparisons will be preferred.

### Stage 3: Interpretation
Interpret results in terms of calibration trade-offs:

- Did the intervention improve self-reliance when AI was wrong?
- Did it preserve the ability to benefit from correct AI advice?
- Did it reduce overreliance without collapsing trust or understanding?

---

## 10. Success Criteria

The intervention will be considered promising if:

### Strong success
- RSR improves clearly,
- RAIR does not substantially decrease,
- and overreliance-related switching is reduced.

### Partial success
- RSR shows an improving trend,
- switch behavior becomes more selective,
- even if trust or convenience decreases slightly.

### Weak result but still informative
- no clear behavioral gain,
- but useful evidence about whether reflective prompts are too weak, too strong, or poorly timed.

Even a non-significant pilot can still be valuable if it clarifies design direction.

---

## 11. Expected Contribution of the Pilot

This pilot is expected to provide:

1. a working implementation of a calibration-aware conversational XAI,
2. initial behavioral evidence about its impact on overreliance,
3. a clearer basis for later scaling the study into a more publication-oriented project.

---

## 12. Current Design Philosophy

The purpose of this project is not to make the conversational AI more persuasive.

The purpose is to make the human-AI interaction **better calibrated**.

That means:
- less blind agreement,
- more appropriate reliance,
- and better support for human judgment under disagreement.