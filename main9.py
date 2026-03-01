import qsharp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

qsharp.init(project_root=".")

indices = ["SP500", "NDX", "FTSE", "RATE", "GOLD", "BBDXY", "WORLD", "MAG7", "AGG", "VIX"]
vols = [0.5, 0.6, 0.4, 0.3, 0.4, 0.3, 0.5, 0.7, 0.2, 0.9]

print("🌌 Generating Quantum Efficient Frontier (500 Portfolios)...")

# 1. Sample the Quantum Market
raw_data = []
for _ in range(1500):
    res = qsharp.eval(f"BloombergQuantum.EncodeGlobalMarket({vols}, 1.0)")
    raw_data.append([int(b) for b in res])
df = pd.DataFrame(raw_data, columns=indices)

# 2. Monte Carlo Weight Generation
results = []
for _ in range(500):
    # Focus on 4 key diversifying assets
    weights = np.random.random(4)
    weights /= np.sum(weights)
    
    # Portfolio = w1*SP500 + w2*GOLD + w3*NDX + w4*AGG
    p_state = (weights[0] * df['SP500'] + 
               weights[1] * df['GOLD'] + 
               weights[2] * df['NDX'] + 
               weights[3] * df['AGG'])
    
    # Avg State is our 'Return' (higher = more assets 'up')
    # Volatility is our 'Risk'
    results.append({
        'Return': 1 - p_state.mean(), 
        'Risk': p_state.std(),
        'Sharpe': (1 - p_state.mean()) / p_state.std()
    })

results_df = pd.DataFrame(results)

# 3. Plotting the Frontier
plt.figure(figsize=(12, 7))
scatter = plt.scatter(results_df['Risk'], results_df['Return'], 
                      c=results_df['Sharpe'], cmap='viridis', alpha=0.6)

plt.colorbar(scatter, label='Quantum Stability Score')
plt.title("Quantum Efficient Frontier: 2026 Market Crash Simulation", fontsize=14)
plt.xlabel("Quantum Volatility (Risk)", fontsize=12)
plt.ylabel("Expected Stability (Return)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

# Highlight the 'Optimal' Portfolio
best = results_df.loc[results_df['Sharpe'].idxmax()]
plt.scatter(best['Risk'], best['Return'], color='red', marker='*', s=200, label='Max Stability')
plt.legend()

plt.show()

print(f"✅ Simulation Complete.")
print(f"🎯 Optimal Quantum Portfolio: Risk {best['Risk']:.3f}, Stability {best['Return']:.3f}")
