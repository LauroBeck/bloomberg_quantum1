import qsharp
import pandas as pd
import matplotlib.pyplot as plt

qsharp.init(project_root=".")

# 10 Indices
indices = ["SP500", "NDX", "FTSE", "RATE", "BCOM", "BBDXY", "WORLD", "MAG7", "AGG", "VIX"]
vols = [0.3, 0.3, 0.3, 0.2, 0.3, 0.2, 0.3, 0.4, 0.1, 0.5]

stress_levels = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
correlations = []

print("📉 Simulating Volatility Regime Shift...")

for level in stress_levels:
    results = []
    for _ in range(500):
        # Calling the updated Q# with the crisisLevel parameter
        r = qsharp.eval(f"BloombergQuantum.EncodeGlobalMarket({vols}, {level})")
        results.append([int(b) for b in r])
    
    df = pd.DataFrame(results, columns=indices)
    # Track the correlation between SP500 and FTSE
    corr_val = df['SP500'].corr(df['FTSE'])
    correlations.append(corr_val)
    print(f"Crisis Level {level:.1f} -> SP-FTSE Correlation: {corr_val:.3f}")

# 📈 Plotting the 'Correlation Break'
plt.figure(figsize=(10, 6))
plt.plot(stress_levels, correlations, marker='o', linestyle='-', color='red')
plt.title("Quantum Market Stress Test: Correlation Convergence")
plt.xlabel("VIX Shock Level (Quantum Entanglement)")
plt.ylabel("SP500 - FTSE Correlation")
plt.grid(True)
plt.show()
