> ⚠️ **DEPRECATED – Old Prototype**
>
> This repository contains the first experimental version of **Sentinel AI**.
> It has now been fully replaced by the modern, stable **Sentinel AI v2**.
>
> Please use the updated version here:
> 👉 https://github.com/DarekDGB/Sentinel-AI-v2
>
> Sentinel AI v2 includes:
> - improved risk detection
> - cleaner architecture
> - full test suite
> - better integration with DQSN and ADN v2
> - future-proof design for the 5-Layer Quantum Shield Network
>
> This repo remains available only for historical reference.


DigiByte-Sentinel-AI

AI-based anomaly detection & threat-monitoring system for the DigiByte blockchain

⸻

Overview

DigiByte-Sentinel-AI is a modular, lightweight, real-time anomaly detection engine designed to enhance the security of the DigiByte blockchain.
It performs continuous analysis of transactions, block patterns, signature entropy, and network behavior using a hybrid statistical–ML model.

The goal is to provide the DigiByte ecosystem with an autonomous early-warning system against:
	•	irregular transaction bursts
	•	potential 51% attack indicators
	•	address behavior drift
	•	low-entropy or weak digital signatures
	•	chain manipulation attempts
	•	suspicious miner activity
	•	cross-chain exploit patterns

⸻

Key Features

1. Real-time anomaly scoring

Extracts 6 core metrics per transaction and assigns a security score from 0.0 to 1.0.

2. Intelligent risk classification
	•	normal
	•	elevated
	•	high
	•	critical

3. Lightweight hybrid model

No GPU required — optimized for running on nodes, servers, or monitoring dashboards.

4. REST API endpoint

Enables wallets, explorers, miners, and exchanges to query the engine:
POST /sentinel/analyze
5. Event logging

Every analyzed transaction includes a timestamp and structured JSON log output.

⸻

Architecture

Data ingestion
	•	Pulls transaction metadata
	•	Computes statistical and behavioral metrics
	•	Feeds vectorized data into the scoring model

Scoring engine

Uses blended weights across:
	•	amount deviation
	•	address recurrence
	•	low-entropy signature detection
	•	frequency anomaly
	•	miner pattern recognition
	•	multi-factor irregularities

Output

JSON object containing:
	•	anomaly score
	•	classification
	•	timestamp
	•	input metrics
Installation
	1.	Clone repository
	2.	Install dependencies:
  pip install fastapi uvicorn numpy
  3.	Run the API:
  uvicorn sentinel_ai:app --host 0.0.0.0 --port 8000
  API Example

Request:
{
  "txid": "abc123",
  "amount": 42000,
  "inputs": 3,
  "outputs": 1,
  "signature_entropy": 0.14,
  "address_reuse": 1
}
Response:
{
  "txid": "abc123",
  "anomaly_score": 0.78,
  "classification": "high",
  "metrics": {
    "amount_zscore": 2.13,
    "freq_score": 0.44,
    "entropy_score": 0.86
  }
}
Security Goals
	•	Strengthen DigiByte’s defense against evolving smart-attack patterns
	•	Provide transparent, open-source monitoring tools for the ecosystem
	•	Offer exchanges and explorers automated anomaly detection
	•	Support future upgrades toward quantum-resilient threat analysis

⸻

Status

This is an open development prototype and can be extended by DigiByte core developers, security researchers, and the wider community.

⸻

License

MIT License — free to use, modify, integrate, or expand.

⸻

Maintainer

Created by DarekDGB
Visionary security concept contributor for the DigiByte ecosystem.
