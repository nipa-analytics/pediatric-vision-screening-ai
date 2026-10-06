import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

from .risk_engine import assess_patient
from .fhir import build_bundle

BASE = Path(__file__).resolve().parents[1]
DATA_PATH = BASE / "data" / "synthetic_patients.json"

app = FastAPI(
    title="Pediatric Vision Responsible AI Prototype",
    version="0.1.0",
    description="Synthetic, non-diagnostic research prototype for workflow and FHIR interoperability testing.",
)


class ResearchInput(BaseModel):
    patient_id: str
    given_name: str = "Child"
    gender: str = "unknown"
    birth_date: Optional[str] = None
    family_history_strabismus_or_amblyopia: Optional[bool] = None
    prematurity_or_low_birth_weight: Optional[bool] = None
    clinician_observed_alignment_concern: Optional[bool] = None
    prior_vision_screen_concern: Optional[bool] = None
    caregiver_visual_behavior_concern: Optional[bool] = None
    developmental_or_neurologic_risk_context: Optional[bool] = None


def load_samples():
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


@app.get("/", response_class=HTMLResponse)
def home():
    samples = load_samples()
    rows = "".join(
        f"<tr><td>{p['patient_id']}</td><td>{p.get('given_name','')}</td><td><a href='/demo/{p['patient_id']}'>Run</a></td></tr>"
        for p in samples
    )
    return f"""
    <html><head><title>Pediatric Vision AI Research Prototype</title>
    <style>
      body{{font-family:Arial,sans-serif;max-width:980px;margin:40px auto;line-height:1.5;padding:0 18px}}
      .warning{{background:#fff3cd;border:1px solid #ffe69c;padding:14px;border-radius:8px}}
      table{{border-collapse:collapse;width:100%;margin-top:20px}} td,th{{border:1px solid #ddd;padding:10px;text-align:left}}
      code{{background:#f3f3f3;padding:2px 5px;border-radius:4px}}
    </style></head><body>
      <h1>Pediatric Vision Responsible AI Prototype</h1>
      <div class='warning'><b>Research only.</b> Synthetic data. Not clinically validated. Not diagnostic and not for patient care.</div>
      <p>This v0.1 prototype demonstrates a clinician-supervised workflow concept using synthetic inputs, an interpretable research-priority engine, abstention for missing data, and FHIR R4 output.</p>
      <h2>Synthetic cases</h2>
      <table><tr><th>ID</th><th>Synthetic name</th><th>Demo</th></tr>{rows}</table>
      <p>API docs: <a href='/docs'>/docs</a></p>
    </body></html>
    """


@app.get("/demo/{patient_id}")
def demo(patient_id: str):
    samples = load_samples()
    record = next((p for p in samples if p["patient_id"] == patient_id), None)
    if not record:
        raise HTTPException(404, "Synthetic patient not found")
    assessment = assess_patient(record)
    return {
        "assessment": assessment.to_dict(),
        "fhir_bundle": build_bundle(record, assessment),
    }


@app.post("/assess")
def assess(input_data: ResearchInput):
    record = input_data.model_dump()
    assessment = assess_patient(record)
    return {
        "assessment": assessment.to_dict(),
        "fhir_bundle": build_bundle(record, assessment),
    }
