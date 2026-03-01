import qsharp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

qsharp.init(project_root=".")

indices = ["SP500", "NDX", "FTSE", "RATE", "GOLD", "BBDXY", "WORLD", "MAG7", "AGG", "VIX"]
vols = [0.5, 0.6, 0.4, 0.3, 0.4, 0.3, 0.5, 0.7, 0.2, 0.9]

print("⚖️ Initializing Quantum Portfolio Optimizer...")
print("🔥 Stress Testing (Crisis Level 1.0)...")

# 1. Generate 2000 Quantum Scenarios
raw_results = []
for _ in range(2000):
    res = qsharp.eval(f"BloombergQuantum.EncodeGlobalMarket({vols}, 1.0)")
    raw_results.append([int(b) for b in res])

df = pd.DataFrame(raw_results, columns=indices)

# 2. Portfolio Strategies
portfolios = {
    "High-Growth Tech": {"NDX": 0.5, "MAG7": 0.5},
    "Traditional 60/40": {"SP500": 0.6, "AGG": 0.4},
    "Quantum Protected": {"SP500": 0.3, "AGG": 0.3, "GOLD": 0.4}
}

# 3. Calculate metrics and store for plotting
names = []
stability_scores = []

print("\n--- Strategy Analysis ---")
for name, weights in portfolios.items():
    p_state = sum(df[asset] * weight for asset, weight in weights.items())
    avg_state = p_state.mean()
    volatility = p_state.std()
    
    # Stability Score: Higher is better (lower volatility/exposure)
    score = (1 - avg_state) / volatility if volatility > 0 else 0
    
    names.append(name)
    stability_scores.append(score)
    print(f"{name}: Stability Score = {score:.3f}")

# --- 4. Plotting Block ---
plt.figure(figsize=(10, 6))
colors = ['#ff9999', '#66b3ff', '#99ff99'] # Red, Blue, Green
bars = plt.bar(names, stability_scores, color=colors, edgecolor='black', alpha=0.8)

# Add value labels on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02, f'{yval:.3f}', ha='center', va='bottom', fontweight='bold')

plt.title("Portfolio Stability Comparison: Level 1.0 Crisis", fontsize=14, fontweight='bold')
plt.ylabel("Stability Score (Risk-Adjusted Protection)", fontsize=12)
plt.ylim(0, max(stability_scores) * 1.2) # Give some space for labels
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Highlight the winner
plt.annotate('Best Protection', xy=(2, stability_scores[2]), xytext=(2, stability_scores[2] + 0.15),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()
