# EHR Risk Signals for Early Pediatric Vision Risk Detection Before Age 3

## Purpose

This document outlines potential electronic health record signals that may support responsible AI-assisted early pediatric vision risk detection before age 3.

The goal is not to diagnose amblyopia, strabismus, or abnormal visual development using EHR data. The goal is to identify early patterns that may help pediatric care teams recognize possible vision-related concerns, review referral needs, and reduce missed follow-up.

## Why EHR Risk Signals Matter

For infants and toddlers, pediatric vision concerns may appear gradually across multiple healthcare encounters.

A single visit may not show enough evidence. However, repeated signals across time may suggest that a child needs professional eye-care evaluation.

Examples:

```text
12-month visit: Parent mentions occasional eye drifting
18-month visit: Pediatrician notes poor fixation
24-month visit: Vision screening attempt incomplete
30-month visit: No completed ophthalmology referral documented
```

Individually, each signal may seem minor. Together, they may indicate a possible referral gap.

This is where EHR-connected AI could support pediatric care teams.

## Potential EHR Risk Signal Categories

## 1. Parent-Reported Concerns

Parent concerns are often one of the earliest indicators.

Possible EHR phrases or structured entries:

* Eye drifting
* Eye turning inward
* Eye turning outward
* Lazy eye concern
* Crossed eyes
* Poor eye contact
* Poor visual tracking
* Child squints frequently
* Child tilts head
* Child closes one eye
* Concern about one eye being weaker
* Concern about abnormal eye movement
* Family noticed eye misalignment

Example AI-supported flag:

```text
Parent-reported vision concern documented. Review for follow-up or referral may be appropriate.
```

## 2. Clinician-Observed Signals

Pediatricians may document observations during well-child visits or clinical encounters.

Possible signals:

* Abnormal fixation
* Abnormal tracking
* Intermittent eye deviation
* Suspected strabismus
* Failed visual behavior assessment
* Poor red reflex concern
* Asymmetric eye movement
* Head tilt observed
* Eye alignment concern
* Unable to complete vision screen
* Concern noted but no referral documented

Example AI-supported flag:

```text
Clinician-observed eye alignment or fixation concern identified. Review for possible pediatric eye-care referral.
```

## 3. Vision Screening Results

Structured screening results can provide important signals.

Possible EHR fields:

* Passed vision screen
* Failed vision screen
* Incomplete vision screen
* Unable to screen
* Uncooperative child
* Instrument-based screening abnormal
* Photoscreening referral recommended
* Visual acuity not testable
* Repeat screening recommended
* No documented follow-up after abnormal result

High-risk combinations:

```text
Failed screen + no referral
Incomplete screen + repeated parent concern
Unable to screen + eye alignment concern
Abnormal screening + missed follow-up
```

Example AI-supported flag:

```text
Vision screening result appears abnormal or incomplete, and follow-up status is unclear.
```

## 4. Referral History

Referral tracking is one of the most important EHR components.

Possible referral signals:

* Ophthalmology referral placed
* Optometry referral placed
* Pediatric ophthalmology referral pending
* Referral not completed
* Appointment missed
* Referral closed without visit
* Specialist visit completed
* Family declined referral
* Referral delayed due to access barrier
* No referral found after documented concern

Example AI-supported flag:

```text
Vision-related concern documented, but no completed eye-care referral is found in the record.
```

## 5. Follow-Up Completion Signals

Early detection only matters if follow-up occurs.

Possible follow-up fields:

* Referral completed
* Appointment scheduled
* Appointment cancelled
* No-show
* Rescheduled
* Specialist note received
* Treatment plan documented
* Follow-up overdue
* Family unreachable
* Insurance/access barrier documented
* No outcome documented

Example AI-supported flag:

```text
Eye-care referral appears incomplete or overdue. Care team review may be needed.
```

## 6. Medical and Developmental Risk Factors

Some children may need closer monitoring due to clinical history.

Possible risk factors:

* Prematurity
* Low birth weight
* Neonatal intensive care history
* Developmental delay
* Neurologic conditions
* Genetic syndromes associated with vision risk
* Family history of strabismus
* Family history of amblyopia
* Prior ocular abnormality
* Craniofacial condition
* History of trauma affecting eye region

These signals should not create diagnosis. They may support risk-aware follow-up.

Example AI-supported flag:

```text
Clinical history includes factors associated with increased need for vision monitoring. Review screening and referral status.
```

## 7. Visit Timeline Patterns

Longitudinal patterns may be more important than one isolated note.

Potential pattern examples:

```text
Parent concern appears across multiple visits
```

```text
Vision screening repeatedly incomplete
```

```text
Referral placed but no completed specialist evaluation
```

```text
Eye concern documented before age 3 but follow-up delayed
```

```text
Risk factors present but no vision screening status documented
```

Example AI-supported flag:

```text
Repeated vision-related signals appear across visits. Review for possible referral or follow-up.
```

## 8. Clinical Note Keywords

Natural language processing could search de-identified clinical notes for relevant terms.

Potential keywords:

```text
eye drift
eye drifting
lazy eye
crossed eye
crossed eyes
eye turn
turning inward
turning outward
wandering eye
poor fixation
poor tracking
abnormal gaze
head tilt
squinting
failed vision screen
unable to screen
vision concern
amblyopia concern
strabismus concern
ophthalmology referral
optometry referral
```

Important: keyword detection alone is not enough. The system must understand context.

For example:

```text
No eye drifting observed
```

should not be treated the same as:

```text
Parent reports eye drifting
```

## 9. Data Quality Issues

EHR data can be incomplete, inconsistent, or ambiguous.

Examples:

* Missing screening result
* Missing referral status
* Vague note language
* Conflicting documentation
* No outcome after referral
* Unclear whether specialist visit occurred
* Image or screening data unavailable
* Parent concern documented without follow-up plan

The system should flag uncertainty rather than create false confidence.

Example output:

```text
Vision-related information is incomplete. Clinical review may be needed if concern persists.
```

## 10. Example Risk Signal Logic

This section describes possible non-diagnostic logic for research planning.

### Low Concern Example

```text
No parent concern documented
No failed screening
No abnormal clinician observation
No risk factor requiring special follow-up
```

Possible output:

```text
No vision-related EHR risk pattern identified at this time.
```

### Moderate Concern Example

```text
Parent concern documented once
No completed vision screening found
No referral documented
```

Possible output:

```text
Vision-related parent concern documented. Consider reviewing screening status.
```

### Higher Concern Example

```text
Repeated parent concern
Incomplete screening attempt
Clinician note mentions poor fixation
No completed referral
```

Possible output:

```text
Repeated vision-related risk signals identified. Clinician review for possible eye-care referral is recommended.
```

### Referral Gap Example

```text
Failed vision screening
Referral recommended
No specialist appointment completed
```

Possible output:

```text
Possible referral gap identified. Follow-up status should be reviewed.
```

## 11. Safe Output Language

The system should use cautious, referral-support language.

Appropriate:

```text
This child may benefit from professional eye-care evaluation.
```

```text
Vision-related concern documented; follow-up status appears incomplete.
```

```text
Repeated risk signals identified across visits. Clinician review is recommended.
```

```text
Data is incomplete. The system cannot determine whether follow-up occurred.
```

Avoid:

```text
This child has amblyopia.
```

```text
This child has strabismus.
```

```text
This child does not need an eye exam.
```

```text
No vision problem exists.
```

## 12. Responsible AI Considerations

Any EHR-based AI system for children must include strong safeguards.

### Privacy

* Use de-identified data for research
* Limit data collection to relevant signals
* Protect child health information
* Follow healthcare privacy requirements in clinical settings

### Safety

* No diagnosis
* No replacement of clinician judgment
* No direct parent-facing medical conclusion
* Clinician review required before action

### Fairness

Evaluate whether risk detection works across:

* Age groups
* Sex
* Race and ethnicity, where ethically and legally appropriate
* Language groups
* Insurance/access categories
* Clinical sites
* Socioeconomic settings
* Children with complex medical histories

### Explainability

The system should explain the reason for a flag.

Example:

```text
Flag reason:
- Parent concern documented at two visits
- Screening incomplete
- No completed eye-care referral found
```

### Human Oversight

AI should support pediatricians, care coordinators, ophthalmologists, optometrists, and hospital quality teams. It should not replace them.

## 13. Potential Validation Metrics

Future clinical collaboration could evaluate:

* Number of EHR risk flags generated
* Clinician agreement with flags
* Referral rate after flag
* Referral completion rate
* Time from first concern to referral
* Time from referral to specialist visit
* Missed follow-up reduction
* False positive rate
* False negative rate
* Bias across demographic and access groups
* Clinician usability
* Family understanding and acceptance

## 14. Research Use in This Repository

At the current independent research stage, this document is a conceptual framework only.

No patient data is used.

The purpose is to support:

* Research planning
* Hospital workflow design
* Responsible AI discussion
* Future IRB-aware study development
* Pediatric vision AI collaboration with clinicians and researchers

## 15. Disclaimer

This document reflects independent research exploration and educational work. It is not intended to provide medical advice, diagnosis, clinical guidance, or a validated medical device. Pediatric vision concerns should always be evaluated by licensed eye-care professionals.

