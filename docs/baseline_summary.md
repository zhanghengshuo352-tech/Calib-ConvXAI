# Baseline Summary

## Paper
**He, G., Aishwarya, N., & Gadiraju, U. (2025).**  
*Is Conversational XAI All You Need? Human-AI Decision Making With a Conversational XAI Assistant.*

## 1. What this paper studies

This paper investigates how a **conversational XAI interface** affects human-AI decision making. The authors focus on three dimensions together:

- user understanding of the AI system,
- user trust in the AI system,
- user reliance on AI recommendations.

The key framing of the paper is that XAI should not be evaluated only by whether users like it more or feel more informed. Instead, the authors ask whether a more interactive explanation interface changes how people actually make decisions with AI. In particular, they compare conversational XAI against a more traditional XAI dashboard and examine whether conversational interaction improves decision quality or instead creates new risks.

---

## 2. Why the paper matters

This paper is important because it moves beyond a simple interface-comparison question.

Its real contribution is to highlight a tension:

**an explanation interface can improve understanding and trust without necessarily improving calibrated human-AI decision making.**

The authors report that conversational XAI can lead to better understanding and higher trust compared with an XAI dashboard, but they also find clear signs of **overreliance** in both dashboard and conversational conditions. They further report that LLM-enhanced conversations amplify overreliance. The paper therefore argues that better explanations do not automatically produce better decisions.

---

## 3. Main findings

The most important findings of the paper are:

1. Conversational XAI can improve user understanding of the AI system relative to an XAI dashboard.  
2. Conversational XAI can increase user trust.  
3. Users under both dashboard and conversational XAI conditions still show clear overreliance on the AI system.  
4. Large-language-model-enhanced conversations make that overreliance stronger.  
5. A possible explanation for this problem is the **illusion of explanatory depth**.

These findings are what make the paper especially useful as a baseline for extension work.

It does not simply say “conversational XAI is better.”  
Instead, it reveals that conversational explanation may be both **helpful** and **risky** at the same time.

---

## 4. Core research value

The core value of the baseline paper is that it studies **understanding, trust, and reliance together**.

This matters because many systems are evaluated mainly in terms of interpretability or subjective trust, but trust alone is not a sufficient target. A user may trust the system more and still use it poorly. The paper’s framing makes it clear that the central problem is not just whether users agree with AI more often, but whether their reliance is **appropriate**.

---

## 5. Why this paper is the right baseline for my project

This paper is the right baseline for my project for three reasons.

First, it already identifies the central problem I want to work on:  
**overreliance in conversational explanation settings.**

Second, it gives a clear design direction for extension work:  
if conversational explanations improve understanding and trust but also increase overreliance, then the next step should not be to make the interface more persuasive. The next step should be to make the interaction **better calibrated**.

Third, it provides a clean conceptual foundation for my own project.  
My proposed extension, **Calib-ConvXAI**, is not trying to replace conversational XAI. It is trying to address one of its most important weaknesses: the tendency for users to over-rely on AI when explanations become more fluent, more interactive, and potentially more convincing.

---

## 6. Limitation that motivates my extension

The baseline paper is strong in diagnosis, but for my purposes it leaves one important gap:

**it identifies overreliance clearly, but it does not itself provide a concrete interaction mechanism for reducing overreliance within the conversational XAI workflow.**

This is the point where my extension begins.

Instead of asking how to make conversational XAI richer or more natural, I ask how to make it **safer and better calibrated** during human-AI decision making. That is the motivation behind disagreement-aware calibration prompting in Calib-ConvXAI.

---

## 7. My takeaway from the baseline

My main takeaway from this paper is:

**Conversational XAI is not only an explanation interface. It is a decision-shaping interface.**

That means the research question should not stop at whether users understand the AI better. It must also ask whether the interface changes user behavior in a beneficial or risky way. The baseline paper shows that conversational XAI may improve understanding and trust, but it also warns that these gains can coexist with overreliance.

For my project, this becomes the central design challenge: how to preserve the benefits of conversational explanations while reducing the risk of blind reliance.