# Pediatric Vision Responsible AI Prototype — v0.1

A synthetic, non-diagnostic research prototype for testing a clinician-supervised pediatric vision AI workflow before age three.

## What v0.1 demonstrates
- Synthetic pediatric research inputs
- Transparent, rule-based research review priority
- Abstention when too much information is missing
- Human/clinician authority preserved by design
- FHIR R4-style `Patient`, `Observation`, `RiskAssessment`, and draft `ServiceRequest` resources
- FastAPI endpoints and interactive API documentation
- Unit tests for priority and abstention behavior

> **Important:** This prototype is not clinically validated and must not be used for diagnosis, screening, referral, treatment, or patient care. The weights and thresholds are illustrative engineering placeholders.

## Run locally

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
- `http://127.0.0.1:8000/` — demo landing page
- `http://127.0.0.1:8000/docs` — interactive API docs

## Example API call

POST `/assess`

```json
{
  "patient_id": "demo-001",
  "given_name": "SyntheticChild",
  "gender": "unknown",
  "birth_date": "2025-01-15",
  "family_history_strabismus_or_amblyopia": true,
  "prematurity_or_low_birth_weight": false,
  "clinician_observed_alignment_concern": true,
  "prior_vision_screen_concern": false,
  "caregiver_visual_behavior_concern": true,
  "developmental_or_neurologic_risk_context": false
}
```

## Repository structure

```text
app/
  main.py          FastAPI application
  risk_engine.py   transparent research-only logic + abstention
  fhir.py          FHIR R4-style resource generation
data/
  synthetic_patients.json
docs/
  research_scope.md
tests/
  test_risk_engine.py
```

## Recommended v0.2
The next version should add a larger synthetic FHIR cohort, referral/follow-up state tracking, structured audit logs, and fairness/missingness evaluation before introducing any learned model.
