# Research scope and guardrails

## Purpose
This prototype operationalizes a high-level research framework for responsible AI-assisted pediatric vision risk support before age three. It is intended to test data flow, interoperability, transparency, abstention, clinician oversight, and referral/follow-up workflow concepts.

## Explicit non-claims
- It does not diagnose amblyopia, strabismus, or any other condition.
- It is not a validated screening tool.
- It is not a medical device.
- It does not make autonomous referral decisions.
- The weights and thresholds are illustrative engineering placeholders only.
- All included patient data are synthetic.

## v0.1 research questions
1. Can structured synthetic pediatric data be represented in a simple FHIR R4 workflow?
2. Can a support layer expose its contributing inputs and abstain when data are insufficient?
3. Can outputs be represented in a way that preserves clinician authority?
4. Can the pathway connect risk-support output to a proposed referral artifact without creating an actual order?
5. What information should be logged for later safety, fairness, and workflow evaluation?

## Next validation layers
1. Replace illustrative rules with a literature-derived research feature specification.
2. Generate a larger synthetic cohort and define data-quality checks.
3. Add fairness stratification and missingness analysis.
4. Add clinician-review simulation and referral/follow-up state tracking.
5. Define retrospective validation endpoints before any model-development claims.
