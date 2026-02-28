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
