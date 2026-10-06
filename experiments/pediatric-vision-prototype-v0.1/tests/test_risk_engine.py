from app.risk_engine import assess_patient


def test_high_priority_case():
    record = {
        "patient_id": "t1",
        "family_history_strabismus_or_amblyopia": True,
        "prematurity_or_low_birth_weight": False,
        "clinician_observed_alignment_concern": True,
        "prior_vision_screen_concern": True,
        "caregiver_visual_behavior_concern": False,
        "developmental_or_neurologic_risk_context": False,
    }
    result = assess_patient(record)
    assert result.research_priority == "high-review-priority"
    assert result.abstained is False


def test_abstention_for_missing_data():
    record = {
        "patient_id": "t2",
        "clinician_observed_alignment_concern": True,
        "developmental_or_neurologic_risk_context": False,
    }
    result = assess_patient(record)
    assert result.research_priority == "abstain"
    assert result.abstained is True
    assert result.illustrative_score is None


def test_routine_case():
    record = {
        "patient_id": "t3",
        "family_history_strabismus_or_amblyopia": False,
        "prematurity_or_low_birth_weight": False,
        "clinician_observed_alignment_concern": False,
        "prior_vision_screen_concern": False,
        "caregiver_visual_behavior_concern": False,
        "developmental_or_neurologic_risk_context": False,
    }
    result = assess_patient(record)
    assert result.research_priority == "routine-review-priority"
    assert result.illustrative_score == 0
