# Bloomberg Quantum Market Simulator

Hybrid Python + Microsoft Q# implementation of a 4-qubit macro market model.

## Model Structure

Qubits represent:

- SP500 (systemic equity risk)
- Nasdaq (tech beta)
- FTSE (global spillover)
- US Rates (discount factor)

Entanglement encodes macro correlations.

## Features

- Volatility amplitude encoding
- Multi-factor entanglement
- Monte Carlo quantum sampling
- Classical correlation extraction

Built using:
- Microsoft Q#
- Python
- NumPy




_____________________________________________________________






# Bloomberg Quantum Macro Engine

A quantum-inspired macro regime detection and shock transmission framework
for analyzing global indexes and Big Oil equities.

This project models financial assets as quantum state vectors where:

|ψ⟩ = α|Bear⟩ + β|Bull⟩

Momentum and volatility determine state rotation.
Measurement yields regime probabilities.

---

## 🔹 Core Files

### PythonQuantumTrendModel.py → Main Engine

This is the production-ready macro engine.

It performs:

- Quantum state encoding of asset returns
- Bullish/Bearish probability measurement
- Regime classification (Bull / Bear / Transition)
- Crude oil shock propagation modeling
- Macro interference detection (Crude × US10Y)
- Rolling time-evolving regime analysis

This file represents the stable macro modeling framework.

---

### NEXTGENVERSION.py → Experimental Engine

This is the research / development branch of the model.

It may include:

- Alternate quantum encoding structures
- Different rotation dynamics
- Modified shock transmission logic
- Experimental macro phase detection
- Advanced entanglement modeling

Used for testing new quantitative ideas before merging into the main engine.

---

## 🔹 System Components

### 1️⃣ Quantum State Encoding

Each asset is transformed into a normalized state vector:

- Volatility controls amplitude magnitude
- Momentum controls rotational phase
- Measurement produces bullish probability

This allows probabilistic regime interpretation rather than binary signals.

---

### 2️⃣ Shock Propagation Logic

Simulates macro shock transmission:

Example:
+5% crude oil shock → estimated response in oil majors

Transmission strength is derived from correlation structure,
interpreted as a quantum coupling proxy.

This allows systemic risk mapping across the oil complex.

---

### 3️⃣ Interference Model (Macro Alignment Detector)

Models interaction between:

- Crude Oil (inflation impulse)
- US 10Y Yield (rate expectations)

We compute an interference term between quantum states.

High positive interference → macro alignment  
High negative interference → macro conflict  
Mid-range → mixed regime  

This helps identify inflation-driven or rate-driven environments.

---

### 4️⃣ Rolling Regime Engine

Uses a rolling window to compute time-evolving quantum states.

Outputs dynamic bullish probabilities over time.

This detects:

- Regime transitions
- Volatility phase shifts
- Oil macro rotations
- Systemic stress periods

---

## 🔹 Why This Matters

Traditional models rely on:

- Static correlation
- Linear regression
- Binary momentum signals

This framework introduces:

- Probabilistic regime modeling
- Phase-based interpretation
- Shock transmission dynamics
- Macro interaction modeling
- Time-evolving regime detection

It provides a higher-dimensional interpretation of market behavior.

---

## 🔹 Target Assets

Indexes:
- S&P 500
- Nasdaq
- US 10Y
- Crude Oil

Big Oil:
- Chevron
- Shell
- PetroChina
- ExxonMobil
- BP
- ConocoPhillips

---

## 🔹 Research Direction

Future extensions may include:

- Portfolio allocation engine
- Backtesting framework
- Regime-aware position sizing
- True quantum circuit implementation (Qiskit)
- Real-time dashboard interface
- Systemic risk early-warning module

---

## 🔹 Disclaimer

This is a research project.
It is not financial advice.
