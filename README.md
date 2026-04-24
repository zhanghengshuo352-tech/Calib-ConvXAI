# Calib-ConvXAI

**Reducing Overreliance in Conversational XAI through Disagreement-Aware Calibration Prompting**

## Overview

This project is a research-oriented extension of the ConvXAI baseline introduced in *Is Conversational XAI All You Need? Human-AI Decision Making With a Conversational XAI Assistant*.

The baseline work studies how conversational XAI affects user understanding, trust, and reliance in human-AI decision making. Its key finding is that conversational explanations may improve understanding and trust, but they do not automatically lead to better calibrated reliance; instead, users may become more likely to over-rely on AI, especially in LLM-enhanced conversational settings.

This repository builds on that tension.

Rather than making conversational explanations more persuasive, this project explores how to make them **better calibrated**.

## Motivation

In human-AI decision making, the goal is not simply to make users trust AI more.

The real goal is to help users rely on AI **appropriately**:

- trust AI when it is helpful,
- question AI when it may be wrong,
- and avoid blindly following persuasive but incorrect recommendations.

The ConvXAI baseline suggests that explanation quality and interaction quality do not automatically translate into better decision calibration.

## Research Question

**Can a calibration-aware conversational XAI reduce overreliance while preserving the understanding and trust benefits of conversational explanations?**

## Proposed Idea

This project proposes **Disagreement-Aware Calibration Prompting**.

The main idea is:

> when the user’s first decision disagrees with the AI recommendation, the system inserts a short calibration prompt before the final decision.

This intervention is designed to slow down unreflective switching and encourage more analytical engagement exactly at the moment where reliance quality matters most.

## Example Calibration Prompt

**Before changing your answer, briefly state which two cues you relied on most.**

This first version is intentionally simple so that the intervention remains lightweight, analyzable, and feasible to implement in a pilot prototype.

## Why This Project

The baseline paper shows that users may agree with AI more often under conversational explanation settings, but increased agreement is not always beneficial.

This project therefore focuses on:

- reducing inappropriate switching,
- improving self-reliance when AI is wrong,
- while preserving the useful parts of conversational explanation.

This direction is also consistent with broader work on overreliance and cognitive forcing, which suggests that explanation alone may not be enough and that reflective interventions can matter.

## Project Goals

This project has three main goals:

1. **Reproduce the ConvXAI baseline**
   - understand the original data flow, measures, and analysis pipeline

2. **Design a calibration-aware extension**
   - implement disagreement-aware calibration prompting

3. **Evaluate whether the extension improves reliance calibration**
   - especially under cases where the user initially disagrees with AI

## Experimental Design

### Pilot Design

The first pilot study will use a **2-condition between-subjects design**:

- **Condition A:** Baseline ConvXAI
- **Condition B:** Calib-ConvXAI

This small pilot is chosen for feasibility and clarity. The goal is to test whether the intervention improves calibration before expanding to more conditions.

### Trigger Rule

The calibration prompt is triggered only when:

- **user first decision ≠ AI recommendation**

This keeps the intervention lightweight and focused on high-risk cases where reliance quality is meaningful, matching the spirit of the baseline paper’s disagreement-sensitive analysis.

## Evaluation Plan

### Primary Measure

- **RSR (Relative positive self-reliance)**  
  Main indicator of whether users can maintain correct self-reliance when the AI is wrong.

### Secondary Measures

- **RAIR**
- **switch fraction**
- **agreement fraction**

### Supporting Measures

- subjective trust
- explanation usefulness
- objective feature understanding

These measures follow the baseline ConvXAI framework, which evaluates understanding, trust, and reliance together rather than treating trust alone as success.

## Baseline

This project is based on the public ConvXAI repository:

**Baseline repository:** `delftcrowd/IUI2025_ConvXAI`

The original repository is a notebook-centered experimental analysis project with public code and data resources for reproducing the paper’s analysis pipeline.

## Repository Structure

```text
Calib-ConvXAI/
├─ README.md
├─ docs/
│  ├─ proposal.md
│  ├─ flow_design.md
│  ├─ literature_map.md
│  └─ experiment_design.md
├─ src/
│  ├─ baseline/
│  ├─ calib_convxai/
│  └─ analysis/
├─ notebooks/
│  ├─ baseline_reproduction.ipynb
│  ├─ pilot_analysis.ipynb
│  └─ figures.ipynb
├─ data/
│  ├─ raw/
│  ├─ processed/
│  └─ data_dictionary.md
├─ results/
│  ├─ figures/
│  ├─ tables/
│  └─ pilot_summary.md
└─ environment.yml