# sentinel_ai.py
# DigiByte Sentinel AI – Real-Time Anomaly Detection Module

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="DigiByte Sentinel AI")

# ----------------------------
# INPUT MODEL
# ----------------------------

class SentinelInput(BaseModel):
    entropy: float
    nonce_repetition: float
    mempool_spike: float
    reorg_depth: float
    tx_size: float

# ----------------------------
# NORMALIZATION HELPERS
# ----------------------------

def clamp01(x):
    return max(0.0, min(1.0, float(x)))

# ----------------------------
# RISK MODEL
# ----------------------------

def compute_risk(entropy, nonce_repetition, mempool_spike, reorg_depth, tx_size):
    weights = np.array([0.30, 0.25, 0.20, 0.15, 0.10], dtype=float)
    metrics = np.array([
        clamp01(1 - entropy),
        clamp01(nonce_repetition),
        clamp01(mempool_spike),
        clamp01(reorg_depth),
        clamp01(tx_size)
    ], dtype=float)
    score = float(np.dot(weights, metrics))
    return clamp01(score)

# ----------------------------
# CLASSIFICATION
# ----------------------------

def classify(score):
    if score < 0.25:
        return "normal"
    if score < 0.50:
        return "elevated"
    if score < 0.75:
        return "high"
    return "critical"

# ----------------------------
# API ROUTE
# ----------------------------

@app.post("/sentinel/analyze")
def analyze(data: SentinelInput):
    score = compute_risk(
        data.entropy,
        data.nonce_repetition,
        data.mempool_spike,
        data.reorg_depth,
        data.tx_size
    )
    level = classify(score)
    return {
        "risk_score": round(score, 4),
        "level": level
    }
