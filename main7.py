import qsharp
import pandas as pd
import numpy as np

# 1. Initialize the quantum environment
qsharp.init(project_root=".")

# Asset Map based on your Q# logic:
# 0:SP500, 1:NDX, 2:FTSE, 3:RATE, 4:GOLD, 5:BBDXY, 6:WORLD, 7:MAG7, 8:AGG, 9:VIX
indices = ["SP500", "NDX", "FTSE", "RATE", "GOLD", "BBDXY", "WORLD", "MAG7", "AGG", "VIX"]
vols = [0.5, 0.6, 0.4, 0.3, 0.4, 0.3, 0.5, 0.7, 0.2, 0.9]

print("⚖️ Initializing Quantum Portfolio Optimizer...")
print("🔥 Stress Testing (Crisis Level 1.0)...")

# 2. Generate 2000 Quantum Scenarios
raw_results = []
for _ in range(2000):
    # Running at crisisLevel 1.0 to trigger your Section B logic
    res = qsharp.eval(f"BloombergQuantum.EncodeGlobalMarket({vols}, 1.0)")
    raw_results.append([int(b) for b in res])

df = pd.DataFrame(raw_results, columns=indices)

# 3. Define Portfolio Weights
portfolios = {
    "High-Growth Tech": {"NDX": 0.5, "MAG7": 0.5},
    "Traditional 60/40": {"SP500": 0.6, "AGG": 0.4},
    "Quantum Protected": {"SP500": 0.3, "AGG": 0.3, "GOLD": 0.4}
}

print("\n" + "="*30)
print("   PORTFOLIO STRESS TEST")
print("="*30)

for name, weights in portfolios.items():
    # Calculate weighted 'performance' (Lower is better in a crash simulation)
    p_state = sum(df[asset] * weight for asset, weight in weights.items())
    
    avg_state = p_state.mean()
    volatility = p_state.std()
    
    # Efficiency Score (Lower average state / Lower volatility = Better Protection)
    # We want a portfolio that doesn't all 'flip to 1' at once.
    score = (1 - avg_state) / volatility if volatility > 0 else 0
    
    print(f"Strategy: {name}")
    print(f"  > Avg 'Down' State: {avg_state:.3f} (Lower is better)")
    print(f"  > Quantum Vol:      {volatility:.3f}")
    print(f"  > Stability Score:  {score:.3f}\n")
