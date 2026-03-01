import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# =============================
# CONFIG
# =============================

assets = {
    "SP500": "^GSPC",
    "NASDAQ": "^IXIC",
    "US10Y": "^TNX",
    "CRUDE": "CL=F",

    # Oil majors
    "CHEVRON": "CVX",
    "SHELL": "SHEL",
    "PETROCHINA": "0857.HK",
    "EXXON": "XOM",
    "BP": "BP",
    "COP": "COP"
}

start_date = "2023-01-01"
rolling_window = 30

# =============================
# DOWNLOAD
# =============================

data = yf.download(
    list(assets.values()),
    start=start_date,
    auto_adjust=True,
    progress=False
)["Close"]

data = data.dropna(axis=1, how="all")
returns = data.pct_change().dropna()

# =============================
# QUANTUM STATE ENCODER
# =============================

def quantum_state(series):
    momentum = series.mean()
    volatility = series.std()

    if volatility == 0:
        return np.array([1, 0])

    theta = np.arctan2(momentum, volatility)
    alpha = np.cos(theta)
    beta = np.sin(theta)

    norm = np.sqrt(alpha**2 + beta**2)
    return np.array([alpha/norm, beta/norm])

def bullish_prob(state):
    return np.abs(state[1])**2


# =============================
# 1️⃣ REGIME CLASSIFIER
# =============================

def classify_regime(prob):
    if prob > 0.65:
        return "BULL"
    elif prob < 0.35:
        return "BEAR"
    else:
        return "TRANSITION"

regime_output = {}

for asset in returns.columns:
    state = quantum_state(returns[asset])
    prob = bullish_prob(state)
    regime_output[asset] = (prob, classify_regime(prob))

print("\n=== QUANTUM REGIME CLASSIFICATION ===\n")
for k, v in regime_output.items():
    print(f"{k}: {v[0]:.3f}  →  {v[1]}")

# =============================
# 2️⃣ SHOCK PROPAGATION SIMULATOR
# =============================

oil_assets = ["CVX", "SHEL", "0857.HK", "XOM", "BP", "COP"]
oil_assets = [a for a in oil_assets if a in returns.columns]

corr_matrix = returns[["CL=F"] + oil_assets].corr()

# Simulate crude shock
shock_size = 0.05  # +5% crude shock
shock_effect = {}

for asset in oil_assets:
    transmission = corr_matrix.loc["CL=F", asset]
    shock_effect[asset] = transmission * shock_size

print("\n=== CRUDE SHOCK PROPAGATION (+5%) ===\n")
for k, v in shock_effect.items():
    print(f"{k}: expected move ≈ {v:.3%}")

# =============================
# 3️⃣ INTERFERENCE MODEL
# (Crude × US10Y interaction)
# =============================

if "CL=F" in returns.columns and "^TNX" in returns.columns:

    crude_state = quantum_state(returns["CL=F"])
    yield_state = quantum_state(returns["^TNX"])

    # Quantum interference term
    interference = np.dot(crude_state, yield_state)

    print("\n=== MACRO INTERFERENCE ===\n")
    print(f"Crude–Yield interference strength: {interference:.3f}")

    if interference > 0.7:
        print("Macro alignment regime")
    elif interference < -0.7:
        print("Macro conflict regime")
    else:
        print("Mixed macro regime")

# =============================
# ROLLING REGIME VISUALIZATION
# =============================

plt.figure(figsize=(12, 6))

for asset in oil_assets:
    probs = []
    for i in range(rolling_window, len(returns)):
        window = returns[asset].iloc[i-rolling_window:i]
        state = quantum_state(window)
        probs.append(bullish_prob(state))

    plt.plot(probs, label=asset)

plt.axhline(0.65, linestyle="--")
plt.axhline(0.35, linestyle="--")

plt.title("Rolling Quantum Regime Probability (Oil Majors)")
plt.ylabel("Bullish Probability")
plt.legend()
plt.tight_layout()
plt.show()
