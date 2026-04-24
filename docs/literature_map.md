# Literature Map

## Literature Map

This project is positioned at the intersection of three literature lines:

1. **Conversational XAI for human-AI decision making**  
2. **Overreliance and reliance calibration in AI-assisted decisions**  
3. **Cognitive forcing / reflective interventions for reducing overreliance**

The core motivation of **Calib-ConvXAI** comes from connecting these three lines into one research gap:  
conversational explanations may improve understanding and trust, but they do not automatically produce better calibrated reliance; therefore, we need a lightweight intervention that reduces overreliance without discarding the benefits of conversational XAI.

---

## 1. Baseline Line: Conversational XAI

### Baseline paper
**He, G., Aishwarya, N., & Gadiraju, U. (2025).**  
*Is Conversational XAI All You Need? Human-AI Decision Making With a Conversational XAI Assistant.*

### Why it matters
This is the direct baseline of the current project. The paper studies how conversational XAI affects user understanding, trust, and reliance in human-AI decision making. Its central result is highly relevant: conversational XAI can improve understanding and trust relative to an XAI dashboard, but users under both dashboard and conversational XAI conditions still show noticeable **overreliance**, and LLM-enhanced conversations amplify that risk. The paper also links this risk to the **illusion of explanatory depth**, making it a strong foundation for a calibration-oriented extension.

### What this paper gives my project
This baseline gives me:
- the main problem framing: understanding, trust, and reliance should be studied together,
- the core tension: better explanations do not guarantee better decision calibration,
- the measurement logic: reliance should be evaluated through behavior-sensitive metrics rather than trust alone.

### Limitation / gap
The baseline paper identifies overreliance as a major problem, but it does not propose a concrete mechanism for reducing it within the conversational XAI interaction itself. That becomes the starting point of my project.

---

## 2. Reliance Calibration Line

### Key paper
**Cao, S., Liu, A., & Huang, C.-M. (2024).**  
*The Roles of AI Uncertainty Presentation, Initial User Decision, and User Demographics in AI-Assisted Decision-Making.*

### Why it matters
This line of work is important because it treats **appropriate reliance** as a design target rather than assuming that more trust is always beneficial. It shows that calibrated uncertainty presentation matters, but also that simply showing model uncertainty alone is not sufficient; the effects depend on how uncertainty is presented and on the user’s own initial decision. This is especially relevant to my project because I also want the intervention to depend on the user’s current decision state, not just on static explanation content.

### What this paper gives my project
This literature tells me:
- appropriate reliance is a better target than raw trust,
- intervention timing and decision context matter,
- user initial judgment should be part of the design logic.

### Limitation / gap
Uncertainty presentation addresses calibration, but it may still be too passive. It does not necessarily force the user to reflect at the moment of disagreement. This suggests that a more interactional mechanism may be needed in conversational XAI settings.

---

## 3. Cognitive Forcing Line

### Key paper
**Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021).**  
*To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.*

### Why it matters
This is one of the strongest papers for my intervention design. It argues that explanations alone do not reliably reduce overreliance and may even increase it. Instead, the authors design **cognitive forcing interventions** that make users engage more analytically with AI recommendations. Their results show that cognitive forcing can significantly reduce overreliance compared with simple XAI approaches, although the most effective interventions tend to receive less favorable subjective ratings.

### What this paper gives my project
This paper gives me the mechanism idea:
- overreliance can be reduced through lightweight reflective friction,
- behavioral improvement may come with a subjective experience trade-off,
- the intervention should target user thinking, not only explanation content.

### Limitation / gap
This work is not specifically about conversational XAI. It provides a mechanism family, but not a conversation-native, disagreement-triggered design. My project therefore adapts its core insight into a conversational setting.

---

## 4. My Research Gap

Putting these three lines together reveals a clear gap:

- ConvXAI shows that conversational explanations can improve understanding and trust, but may worsen overreliance.  
- Appropriate reliance research shows that calibration depends on decision context and user state, not just on explanation transparency.  
- Cognitive forcing research shows that reflective interventions can reduce overreliance, but it does not yet provide a conversational, disagreement-aware mechanism.  

**Therefore, the missing piece is a conversational XAI design that introduces calibration support exactly when the user is at higher risk of being misled.**

---

## 5. Position of Calib-ConvXAI

My project sits here:

- **Baseline:** ConvXAI  
- **Problem:** overreliance in conversational explanation settings  
- **Mechanism source:** cognitive forcing / reflective prompting  
- **Design principle:** trigger intervention only when user–AI disagreement occurs  
- **Goal:** improve reliance calibration without discarding the understanding/trust benefits of conversation.

In this sense, **Calib-ConvXAI** is not trying to replace conversational XAI.  
It is trying to make conversational XAI **safer and better calibrated**.

---

## 6. Working Research Question

**Can a disagreement-aware calibration prompt reduce overreliance in conversational XAI while preserving the benefits of conversational explanations for understanding and trust?**

---

## 7. Working Claim

My current working claim is:

**Compared with baseline ConvXAI, a calibration-aware conversational XAI can improve reliance calibration, especially by helping users maintain correct self-reliance when AI recommendations are wrong.**

---

## 8. Current Takeaway

At the current stage, I do not see my project as “building a smarter chatbot.”  
I see it as designing a **better human-AI decision interaction**, where the objective is not more persuasion, but better-calibrated reliance. That positioning is what makes the project more research-oriented and potentially publication-worthy.