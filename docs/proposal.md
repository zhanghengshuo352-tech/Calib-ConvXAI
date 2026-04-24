# Calib-ConvXAI

## Title
**Calib-ConvXAI: Reducing Overreliance in Conversational XAI through Disagreement-Aware Calibration Prompting**

## 1. Background
Conversational XAI has been shown to improve user understanding and trust compared with static XAI dashboards. However, existing evidence also suggests that these interfaces can increase overreliance on AI, especially when conversations are further enhanced by LLM-based agents. In other words, more interactive and persuasive explanations do not automatically lead to better calibrated human-AI decision making.

The baseline paper for this project is **“Is Conversational XAI All You Need? Human-AI Decision Making With a Conversational XAI Assistant”**, and its public code repository is available on GitHub.

## 2. Problem Statement
The core problem is not whether conversational explanations are more engaging, but whether they help users rely on AI appropriately.

A conversational interface may make users feel that the AI is easier to understand and more trustworthy. However, this does not guarantee that users will make better decisions. In fact, they may become more likely to follow incorrect AI advice. The original ConvXAI paper explicitly highlights this tension and links it to the illusion of explanatory depth.

## 3. Research Gap
Existing ConvXAI work shows the benefits of conversational explanations, but also reveals a risk of overreliance. Existing work on cognitive forcing functions shows that lightweight interventions can reduce overreliance, though often at some cost to subjective user experience. What is still missing is a **conversation-native, conditionally triggered calibration mechanism** for conversational XAI.

More specifically, there is a gap in designing interventions that:
- act only when the user is at higher risk of being misled,
- are embedded naturally into the conversational explanation flow,
- and aim to improve reliance calibration rather than just trust or satisfaction.

## 4. Proposed Idea
This project proposes **Disagreement-Aware Calibration Prompting** for conversational XAI.

The main idea is simple:  
when the user’s initial judgment disagrees with the AI recommendation, the system inserts a short calibration prompt before the final decision.

This intervention is designed to slow down unreflective switching and encourage more analytical engagement exactly at the moment where reliance quality matters most. This design is motivated by two observations:
1. The ConvXAI paper evaluates reliance quality through disagreement-sensitive measures such as switching and relative reliance metrics.
2. Prior work shows that cognitive forcing interventions can significantly reduce overreliance compared with standard explainable AI approaches.

## 5. Research Question
**Can a calibration-aware conversational XAI reduce overreliance while preserving the understanding and trust benefits of conversational explanations?**

## 6. Hypotheses
### H1
Compared with baseline ConvXAI, Calib-ConvXAI will improve **RSR** by helping users maintain their correct judgment when the AI is wrong. This is important because overreliance is most visible when users abandon a correct initial answer in favor of an incorrect AI suggestion.

### H2
Calib-ConvXAI will reduce inappropriate switching while maintaining comparable or only slightly reduced **RAIR**, meaning that users should still be able to adopt correct AI advice when needed.

### H3
Calib-ConvXAI may slightly reduce subjective convenience or smoothness, but it will improve reliance calibration. This trade-off is plausible because prior cognitive forcing research found lower subjective ratings for interventions that reduced overreliance the most.

## 7. Method
### Experimental Design
The first pilot study will use a **2-condition between-subjects design**:

- **Condition A:** Baseline ConvXAI  
- **Condition B:** Calib-ConvXAI

This small pilot design is chosen for feasibility and clarity. The goal is to test whether the intervention improves calibration before expanding to more conditions.

### Trigger Rule
The calibration prompt is triggered only when:
- the user’s first decision is different from the AI recommendation.

This trigger focuses the intervention on high-risk cases where reliance quality is meaningful.

### Example Prompt
A first version can use one lightweight reflection prompt such as:

**“Before changing your answer, briefly state which two cues you relied on most.”**

This version is intentionally simple, so that the intervention remains lightweight and easy to implement.

## 8. Measures
### Primary Measure
- **RSR**  
Main indicator of whether users can maintain correct self-reliance when the AI is wrong.

### Secondary Measures
- **RAIR**
- **switch fraction**
- **agreement fraction**

### Supporting Measures
- subjective trust
- explanation usefulness
- objective feature understanding

These measures align with the original ConvXAI evaluation logic, which focuses on understanding, trust, and reliance in human-AI decision making.

## 9. Expected Contribution
This project aims to make three contributions:

1. **Mechanism contribution**  
   Introduce a disagreement-aware calibration mechanism for conversational XAI.

2. **System contribution**  
   Build a working prototype of Calib-ConvXAI.

3. **Empirical contribution**  
   Evaluate whether this mechanism improves reliance calibration instead of merely increasing trust or engagement.

## 10. Repository Plan
This project will be presented as a research-oriented GitHub repository rather than only a code dump.  
The repository will include:
- background and proposal
- baseline reproduction notes
- intervention design
- pilot experiment setup
- analysis notebooks
- result summaries
- limitations and future directions

## 11. Current Positioning
This project is intended as:
- an extension of the ConvXAI baseline,
- a first personal research project on GitHub,
- and a possible starting point for a more publication-oriented follow-up study.