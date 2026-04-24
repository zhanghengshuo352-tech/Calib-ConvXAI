# Flow Design for Calib-ConvXAI

## 1. Baseline ConvXAI Flow

Task shown to user  
→ User makes **first decision**  
→ AI recommendation and conversational explanation are shown  
→ User makes **final decision**  
→ System records:
- first choice
- final choice
- AI recommendation
- correctness
- switching behavior
- reliance-related measures

This is the basic human-AI decision structure used in the ConvXAI setting.

---

## 2. Calib-ConvXAI Flow

Task shown to user  
→ User makes **first decision**  
→ System checks whether **first decision ≠ AI recommendation**  
→ If **no disagreement**, continue as normal  
→ If **disagreement exists**, trigger **calibration prompt**  
→ User briefly reflects on their current reasoning  
→ AI recommendation and conversational explanation are shown  
→ User makes **final decision**  
→ System records:
- first choice
- final choice
- AI recommendation
- correctness
- calibration prompt response
- switching behavior
- reliance-related measures

---

## 3. Design Logic

The intervention is not always on.  
It appears only when the user and AI disagree, because this is the point where:

- switching is meaningful,
- reliance quality can be judged,
- and overreliance risk becomes most relevant.

The design goal is not to block AI use, but to introduce a short reflective pause before users change their answer.

---

## 4. Calibration Prompt Options

### Option A: Evidence Reflection
“Before changing your answer, briefly state which two cues you relied on most.”

### Option B: Counter-Check
“The AI may still be wrong. What part of the recommendation would you challenge first?”

### Option C: Confidence Checkpoint
“How confident are you in your first decision, and what would make you revise it?”

### Recommended First Version
Use **Option A** first.  
It is the simplest, least fragile, and easiest to analyze in a pilot study.

---

## 5. Main Claim of the Flow

Baseline ConvXAI may increase agreement with AI.  
Calib-ConvXAI aims to make that agreement **better calibrated**, especially in cases where the AI is wrong.