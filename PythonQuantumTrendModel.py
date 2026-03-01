import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# =============================
# CONFIGURATION
# =============================

assets = {
    # Indexes
    "SP500": "^GSPC",
    "NASDAQ": "^IXIC",
    "FTSE100": "^FTSE",
    "US10Y": "^TNX",
    "CRUDE": "CL=F",

    # Big Oil
    "CHEVRON": "CVX",
    "SHELL": "SHEL",
    "PETROCHINA": "0857.HK",     # Fixed (Hong Kong listing)
    "EXXON": "XOM",
    "ARAMCO": "2222.SR",
    "BP": "BP",
    "CONOCOPHILLIPS": "COP"
}

start_date = "2023-01-01"
rolling_window = 30  # for time-evolving quantum states

# =============================
# DOWNLOAD DATA
# =============================

print("Downloading market data...")

data = yf.download(
    list(assets.values()),
    start=start_date,
    auto_adjust=True,
    progress=True
)["Close"]

# Remove assets that failed completely
data = data.dropna(axis=1, how="all")

# Compute returns
returns = data.pct_change().dropna()

if returns.empty:
    raise ValueError("No valid return data downloaded.")

# =============================
# QUANTUM STATE ENCODER
# =============================

def quantum_state_from_returns(series):
    momentum = series.mean()
    volatility = series.std()

    if volatility == 0:
        return np.array([1, 0])

    theta = np.arctan2(momentum, volatility)

    alpha = np.cos(theta)
    beta = np.sin(theta)

    norm = np.sqrt(alpha**2 + beta**2)
    return np.array([alpha/norm, beta/norm])


# =============================
# BUILD STATIC QUANTUM STATES
# =============================

quantum_states = {}

for col in returns.columns:
    if returns[col].isna().all():
        continue
    quantum_states[col] = quantum_state_from_returns(returns[col])

# =============================
# MEASUREMENT (Bullish Prob)
# =============================

bullish_prob = {}

for asset, state in quantum_states.items():
    bullish_prob[asset] = np.abs(state[1])**2

print("\n=== Quantum Bullish Probability ===\n")
for asset, prob in bullish_prob.items():
    print(f"{asset}: {prob:.3f}")

# =============================
# OIL ENTANGLEMENT MATRIX
# (Correlation → Quantum Coupling)
# =============================

oil_assets = [
    ticker for ticker in returns.columns
    if ticker in ["CVX", "SHEL", "0857.HK", "XOM", "2222.SR", "BP", "COP", "CL=F"]
]

oil_returns = returns[oil_assets]
entanglement_matrix = oil_returns.corr()

print("\n=== Oil Entanglement Matrix (Correlation Proxy) ===\n")
print(entanglement_matrix.round(3))

# =============================
# TIME-EVOLVING QUANTUM STATES
# =============================

rolling_quantum_prob = {}

for asset in returns.columns:
    probs = []
    for i in range(rolling_window, len(returns)):
        window_data = returns[asset].iloc[i-rolling_window:i]
        state = quantum_state_from_returns(window_data)
        probs.append(np.abs(state[1])**2)
    rolling_quantum_prob[asset] = probs

# =============================
# VISUALIZATION
# =============================

plt.figure(figsize=(12, 6))
plt.bar(bullish_prob.keys(), bullish_prob.values())
plt.xticks(rotation=90)
plt.title("Quantum Bullish Probability by Asset")
plt.ylabel("Probability")
plt.tight_layout()
plt.show()

# Rolling visualization (Oil only)
plt.figure(figsize=(12, 6))

for asset in oil_assets:
    plt.plot(
        rolling_quantum_prob[asset],
        label=asset
    )

plt.title("Rolling Quantum Bullish Probability (Oil & Crude)")
plt.xlabel("Time")
plt.ylabel("Bullish Probability")
plt.legend()
plt.tight_layout()
plt.show()
