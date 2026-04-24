# Project TODO

## Current Stage
This project is currently at the **research framing and repository setup stage**.

The baseline paper has been selected, the main research tension has been identified, and the extension idea has been formulated. The next goal is to turn the idea into a minimal but concrete research prototype.

---

## Phase 1 — Repository Foundation

### 1. Finalize repository skeleton
- [x] create the root repository folder `Calib-ConvXAI`
- [x] create core folders:
  - [x] `docs/`
  - [x] `src/`
  - [x] `notebooks/`
  - [x] `data/`
  - [x] `results/`
- [x] add initial files:
  - [x] `README.md`
  - [x] `docs/proposal.md`
  - [x] `docs/flow_design.md`
  - [x] `docs/literature_map.md`
  - [x] `docs/experiment_design.md`

### 2. Clean up research positioning
- [x] make sure the project title is consistently written as **Calib-ConvXAI**
- [x] ensure all documents use the same research question
- [x] ensure all documents use the same intervention name:
  - [x] **Disagreement-Aware Calibration Prompting**

### 3. Decide repository visibility strategy
- [x] keep the repo **private** during the setup stage
- [ ] make it public only after the first documentation set is complete

---

## Phase 2 — Baseline Understanding Consolidation

### 4. Baseline reproduction notes
- [ ] create `notebooks/baseline_reproduction.ipynb`
- [ ] document how the original ConvXAI pipeline works
- [ ] summarize:
  - [ ] data input
  - [ ] `util.py`
  - [ ] `calc_measures.py`
  - [ ] H1 / H2 / H3 notebook roles

### 5. Key measures understanding
- [ ] write a short note on:
  - [ ] accuracy
  - [ ] agreement fraction
  - [ ] switch fraction
  - [ ] RAIR
  - [ ] RSR
- [ ] explain in plain language why **RSR** is the main measure for the extension study

### 6. Prepare a concise baseline summary
- [x] create `docs/baseline_summary.md`
- [x] summarize the baseline paper in 1–2 pages
- [x] clearly state:
  - [x] what the baseline found
  - [x] what limitation it leaves open
  - [x] why my project is a meaningful extension

---

## Phase 3 — Intervention Design

### 7. Finalize the first intervention version
- [x] confirm trigger rule:
  - [x] first decision ≠ AI recommendation
- [x] confirm prompt:
  - [x] **“Before changing your answer, briefly state which two cues you relied on most.”**
- [x] keep the first version simple and lightweight

### 8. Create interaction specification
- [x] write `docs/interface_logic.md`
- [x] describe:
  - [x] baseline interaction flow
  - [x] calibration-aware interaction flow
  - [x] what gets recorded at each step
- [x] define exactly when the calibration layer appears

### 9. Decide prototype scope
- [x] use a **minimal prototype**
- [x] avoid building a full-scale chatbot system in the first round
- [x] focus on:
  - [x] fixed task structure
  - [x] fixed AI recommendations
  - [x] fixed explanation content
  - [x] conditional calibration prompt insertion

---

## Phase 4 — Prototype Implementation

### 10. Build the first working prototype
- [ ] create `src/baseline/`
- [ ] create `src/calib_convxai/`
- [ ] implement:
  - [ ] baseline flow
  - [ ] disagreement detection
  - [ ] calibration prompt trigger
  - [ ] response recording
  - [ ] final decision logging

### 11. Create a recordable data structure
- [ ] define what each task log should store:
  - [ ] participant ID
  - [ ] condition
  - [ ] task ID
  - [ ] first decision
  - [ ] AI recommendation
  - [ ] disagreement flag
  - [ ] calibration prompt response
  - [ ] final decision
  - [ ] correctness
  - [ ] switching
  - [ ] optional confidence / time

### 12. Save outputs cleanly
- [ ] create processed output format in `data/processed/`
- [ ] write `data/data_dictionary.md`
- [ ] define field meanings clearly

---

## Phase 5 — Pilot Preparation

### 13. Prepare pilot study materials
- [ ] create task set for pilot
- [ ] define the two conditions:
  - [ ] Baseline ConvXAI
  - [ ] Calib-ConvXAI
- [ ] prepare participant instructions
- [ ] prepare consent / information text if needed

### 14. Define analysis notebook
- [ ] create `notebooks/pilot_analysis.ipynb`
- [ ] calculate:
  - [ ] RSR
  - [ ] RAIR
  - [ ] switch fraction
  - [ ] agreement fraction
- [ ] add descriptive statistics and comparison outputs

### 15. Prepare result summary template
- [x] create `results/pilot_summary.md`
- [ ] include:
  - [ ] main question
  - [ ] setup
  - [ ] key metrics
  - [ ] preliminary findings
  - [ ] limitations
  - [ ] next steps

---

## Phase 6 — GitHub Presentation

### 16. Make the repo look like a research project
- [x] ensure `README.md` is polished
- [ ] add a short project status section
- [ ] add one clean flow diagram or screenshot
- [x] keep folder names consistent
- [ ] remove messy temporary files before publishing

### 17. Prepare public-facing documentation
- [ ] check grammar and consistency in docs
- [x] make sure the project goal is clear
- [ ] make sure the repo is understandable even without personal explanation

### 18. Publish the first version
- [x] create the GitHub repo
- [x] push the structured project
- [ ] keep version 1 focused and clean
- [ ] treat the public repo as the start of a long-term research record

---

## Immediate Next Actions

### This week
- [x] create the repo folder structure locally
- [x] place all current documentation drafts into `docs/`
- [x] finalize `README.md`
- [x] write `docs/baseline_summary.md`

### Next step after that
- [ ] design the prototype interaction logic in code
- [ ] decide how the calibration prompt will be implemented in the interface
- [ ] start building the minimal prototype

---

## Working Principle

This project should be developed as a **research artifact**, not just a code collection.

That means:
- each new feature should answer a research question,
- each design choice should have a clear reason,
- and each result should be recorded clearly, even if the result is negative or incomplete.