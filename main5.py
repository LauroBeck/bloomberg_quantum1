import qsharp
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

qsharp.init(project_root=".")

# 10 Indices in order: SP, NDX, FTSE, RATE, BCOM, BBDXY, WORLD, MAG7, AGG, VIX
indices = ["SP500", "NDX", "FTSE", "RATE", "BCOM", "BBDXY", "WORLD", "MAG7", "AGG", "VIX"]
vols = [0.4, 0.5, 0.3, 0.2, 0.4, 0.3, 0.4, 0.6, 0.1, 0.5]

print("🚀 Running 10-Index Global Quantum Simulation...")

raw_results = []
for _ in range(1000):
    # Pass the list of 10 vols to Q#
    res = qsharp.eval(f"BloombergQuantum.EncodeGlobalMarket({vols}, 0.0)")
    raw_results.append([int(b) for b in res])

# Create DataFrame and Heatmap
df = pd.DataFrame(raw_results, columns=indices)
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, cmap='RdYlGn', center=0)
plt.title("Bloomberg 10-Index Quantum Correlation Matrix (2026)")
plt.show()
