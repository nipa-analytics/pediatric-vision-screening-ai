# Hospital-Based Pediatric Vision AI Workflow Before Age 3

## Purpose

This document outlines a proposed hospital and pediatric healthcare workflow for responsible AI-assisted early pediatric vision risk detection before age 3.

The goal is not to diagnose amblyopia, strabismus, or other pediatric eye conditions using AI. The goal is to support earlier identification of children who may need professional eye-care evaluation by helping pediatric care teams recognize risk signals, track referral gaps, and reduce missed follow-up.

## Why Hospital Workflow Matters

For children under 3, school-based vision screening may be too late or not yet available. Infants and toddlers are more likely to interact with healthcare systems through:

* Well-child visits
* Pediatric primary care appointments
* Vaccination visits
* Developmental checkups
* Hospital encounters
* Neonatal or premature infant follow-up
* Parent-reported concerns

These touchpoints create opportunities to detect early pediatric vision risk before avoidable delays occur.

## High-Level Workflow

```text
Child under age 3 attends pediatric visit or hospital encounter
        ↓
Vision-related information is captured
        ↓
AI-assisted risk layer reviews available signals
        ↓
Data quality and uncertainty are checked
        ↓
Possible risk is flagged for clinician review
        ↓
Pediatrician or care team reviews the flag
        ↓
Referral is placed when appropriate
        ↓
Follow-up completion is tracked in the EHR
        ↓
Outcome data supports future validation
```

## Step 1: Pediatric Visit or Hospital Encounter

The workflow begins when an infant or toddler interacts with the healthcare system.

Possible settings include:

* Pediatric clinic
* Hospital outpatient department
* Well-child visit
* Neonatal follow-up clinic
* Developmental assessment visit
* Emergency or urgent care encounter
* Community health program connected to a healthcare system

At this stage, the system should not assume a diagnosis. It should only collect or recognize possible early signals.

## Step 2: Capture Early Vision-Related Signals

Vision-related risk signals may come from structured or unstructured data.

### Parent-Reported Signals

Examples:

* Parent reports one eye drifting
* Parent notices poor eye contact
* Parent observes frequent squinting
* Parent reports head tilting
* Parent says the child does not track objects well
* Parent notices one eye turning inward or outward
* Parent reports concern but no specialist visit has occurred

### Clinician-Observed Signals

Examples:

* Pediatrician notes abnormal fixation
* Concern about eye alignment
* Incomplete visual behavior assessment
* Abnormal red reflex concern
* Head tilt or facial turning observed
* Failed or incomplete vision screening attempt
* Developmental concern linked to visual behavior

### Structured EHR Signals

Examples:

* Age under 3
* Prematurity
* Neonatal risk factors
* Family history of strabismus or amblyopia
* Prior failed screening
* Prior referral placed
* Referral not completed
* Missed specialist appointment
* No documented follow-up after concern

### Image or Screening Signals

If available, these may include:

* Eye image
* Face image
* Screening device output
* Image quality score
* Eye visibility
* Head position
* Gaze or alignment-related features

## Step 3: AI-Assisted Risk Signal Review

The AI-assisted layer reviews available information to identify possible risk patterns.

The system may analyze:

* Repeated parent concerns
* Clinical note language related to eye drifting or fixation
* Missed referral patterns
* Incomplete screening attempts
* Risk factors across multiple visits
* Image or screening quality issues
* Lack of follow-up after documented concern

The system should not produce a diagnosis.

It should only identify cases that may need clinician review.

## Step 4: Data Quality and Uncertainty Check

Before generating any flag, the system should check whether the available data is reliable.

Examples of uncertainty include:

* Image is blurry
* Child is not facing forward
* Eye region is not visible
* Screening attempt was incomplete
* Clinical note is vague
* Risk signal appears only once
* Data is missing or inconsistent

If the information is insufficient, the system should say:

```text
Data is insufficient for risk interpretation. Clinical review may be needed if concern persists.
```

The system should avoid false reassurance when data quality is poor.

## Step 5: Clinician-Facing Risk Flag

If possible risk patterns are detected, the system generates a clinician-facing summary.

Example output:

```text
Possible pediatric vision risk signal identified.

Reason:
- Parent concern about intermittent eye drifting documented
- Prior vision screening attempt incomplete
- No completed eye-care referral found in record

Suggested action:
Clinician review for possible referral to pediatric ophthalmology or optometry.
```

The output should be short, explainable, and reviewable.

## Step 6: Pediatrician or Care Team Review

The pediatrician or care team reviews the AI-supported flag.

The clinician decides whether the child needs:

* Repeat screening
* Parent education
* Ophthalmology referral
* Optometry referral
* Developmental follow-up
* Watchful waiting with documentation
* No action at that time

AI should support clinical judgment, not replace it.

## Step 7: Referral Pathway

If the clinician determines that referral is appropriate, the system should support a clear referral pathway.

Possible referral destinations:

* Pediatric ophthalmology
* Pediatric optometry
* Orthoptics clinic
* Hospital eye clinic
* Community eye-care partner
* Vision screening follow-up program

The referral should include:

* Reason for referral
* Relevant clinical notes
* Parent concern history
* Screening result or image-quality concern
* Urgency level
* Follow-up instructions

## Step 8: Follow-Up Tracking

The workflow should not end when a referral is placed.

The system should track whether follow-up actually happened.

Follow-up tracking may include:

* Referral placed
* Appointment scheduled
* Appointment completed
* Appointment missed
* Family unable to access care
* Specialist evaluation completed
* Treatment or monitoring plan documented
* No follow-up documented

This is important because early detection only matters if the child reaches care.

## Step 9: Outcome Documentation

If specialist evaluation occurs, outcome data can help future validation.

Possible outcome fields:

* Normal exam
* Strabismus identified
* Amblyopia risk factor identified
* Refractive error identified
* Further monitoring recommended
* Treatment started
* Follow-up needed
* Referral closed

This information can help evaluate whether the AI-assisted workflow improves referral timing and reduces missed cases.

## Proposed End-to-End Workflow Diagram

```text
Infant / toddler under age 3
        ↓
Pediatric visit or hospital encounter
        ↓
Parent concern + clinical observation + EHR history + screening/image data
        ↓
AI-assisted risk signal review
        ↓
Quality and uncertainty check
        ↓
Clinician-facing risk summary
        ↓
Pediatrician / care team review
        ↓
Referral decision
        ↓
Pediatric ophthalmology / optometry evaluation
        ↓
Follow-up completion tracked in EHR
        ↓
Outcome data used for validation and workflow improvement
```

## Safe Output Language

The system should use referral-support language.

Appropriate examples:

```text
This child may benefit from professional eye-care evaluation.
```

```text
Vision-related concern documented; follow-up status appears incomplete.
```

```text
Image or screening quality is insufficient. Clinical review may be appropriate if concern persists.
```

```text
Repeated risk signals identified across visits. Review for possible referral is recommended.
```

The system should not say:

```text
This child has amblyopia.
```

```text
This child has strabismus.
```

```text
No eye problem detected.
```

```text
No referral is needed.
```

## Responsible AI Requirements

A hospital-based pediatric vision AI workflow should include:

* Clinician review before action
* Non-diagnostic output language
* Referral-focused recommendations
* Image and data quality checks
* Uncertainty handling
* EHR-integrated follow-up tracking
* Child privacy protection
* Bias and fairness monitoring
* Explainable risk summaries
* Ongoing validation in real-world pediatric settings

## Key Metrics for Future Validation

Future clinical collaboration could evaluate:

* Number of risk flags generated
* Percentage reviewed by clinicians
* Referral rate after AI-supported flag
* Referral completion rate
* Time from concern to referral
* Time from referral to specialist evaluation
* False positive rate
* False negative rate
* Missed follow-up reduction
* Performance across age groups and demographics
* Clinician usability and trust
* Parent understanding and acceptance

## Research Importance

This workflow reframes pediatric vision AI as a healthcare-system problem, not only a computer vision problem.

For children under 3, the challenge is not only detecting an image pattern. The challenge is ensuring that early concerns are recognized, reviewed, referred, and followed up before avoidable delays occur.

## Current Status

This is an independent research concept and workflow framework.

No patient data is used in this repository. This document is intended to support responsible AI research planning, clinical collaboration discussions, and future IRB-aware study design.

## Disclaimer

This document reflects independent research exploration and educational work. It is not intended to provide medical advice, diagnosis, clinical guidance, or a validated medical device. Pediatric vision concerns should always be evaluated by licensed eye-care professionals.

