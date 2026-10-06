from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

# IMPORTANT: These weights are illustrative only. They are not clinically validated
# and must not be used for diagnosis, screening, referral decisions, or patient care.
SIGNAL_WEIGHTS = {
    "family_history_strabismus_or_amblyopia": 2,
    "prematurity_or_low_birth_weight": 1,
    "clinician_observed_alignment_concern": 3,
    "prior_vision_screen_concern": 3,
    "caregiver_visual_behavior_concern": 1,
    "developmental_or_neurologic_risk_context": 1,
}

REQUIRED_FIELDS = list(SIGNAL_WEIGHTS.keys())

@dataclass
class ResearchAssessment:
    patient_id: str
    status: str
    research_priority: str
    illustrative_score: Optional[int]
    data_completeness: float
    triggered_signals: List[str]
    rationale: List[str]
    abstained: bool
    disclaimer: str

    def to_dict(self) -> Dict:
        return asdict(self)


def assess_patient(record: Dict) -> ResearchAssessment:
    """Return a transparent, research-only priority assessment.

    The engine deliberately abstains when fewer than 60% of the research signals
    are present. The score and thresholds are illustrative and are NOT clinical.
    """
    patient_id = str(record.get("patient_id", "unknown"))
    present = [k for k in REQUIRED_FIELDS if record.get(k) is not None]
    completeness = len(present) / len(REQUIRED_FIELDS)

    disclaimer = (
        "Research prototype only. Not clinically validated. Not a diagnosis, "
        "medical device, screening tool, or referral recommendation. Clinician "
        "judgment remains authoritative."
    )

    if completeness < 0.60:
        return ResearchAssessment(
            patient_id=patient_id,
            status="insufficient-data",
            research_priority="abstain",
            illustrative_score=None,
            data_completeness=round(completeness, 2),
            triggered_signals=[],
            rationale=["Prototype abstained because too many research inputs were missing."],
            abstained=True,
            disclaimer=disclaimer,
        )

    triggered = [k for k, w in SIGNAL_WEIGHTS.items() if record.get(k) is True]
    score = sum(SIGNAL_WEIGHTS[k] for k in triggered)

    # Illustrative tiers for workflow testing only.
    if score >= 5:
        priority = "high-review-priority"
    elif score >= 2:
        priority = "moderate-review-priority"
    else:
        priority = "routine-review-priority"

    rationale = [
        f"{k.replace('_', ' ')} contributed {SIGNAL_WEIGHTS[k]} illustrative point(s)."
        for k in triggered
    ] or ["No positive research signals were present in the available synthetic data."]

    return ResearchAssessment(
        patient_id=patient_id,
        status="complete",
        research_priority=priority,
        illustrative_score=score,
        data_completeness=round(completeness, 2),
        triggered_signals=triggered,
        rationale=rationale,
        abstained=False,
        disclaimer=disclaimer,
    )
