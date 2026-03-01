import qsharp
from collections import Counter
import numpy as np

# 1. Initialize the project (Points to your .qs file folder)
qsharp.init(project_root=".")

print("=== 4-Qubit Macro Market Simulation ===")

shots = 1000
results = []

# 2. Optimized loop: Indentation Fixed
for _ in range(shots):
    # This line is now correctly indented inside the 'for' block
    r = qsharp.eval("BloombergQuantum.EncodeMarketState(0.4, 0.6, 0.3, 0.5)")
    results.append(tuple(r)) 

counts = Counter(results)

print("\nState Distribution (Binary: SP, NDX, FTSE, RATE):")
# Use a fresh counter logic to ensure labels match reality
for state, count in counts.items():
    # Convert each individual element in the tuple 'state' correctly
    b_sp   = 1 if state[0] == 1 or state[0] is True else 0
    b_ndx  = 1 if state[1] == 1 or state[1] is True else 0
    b_ftse = 1 if state[2] == 1 or state[2] is True else 0
    b_rate = 1 if state[3] == 1 or state[3] is True else 0
    
    clean_label = (b_sp, b_ndx, b_ftse, b_rate)
    print(f"State {clean_label} → {count} occurrences")

# -----------------------------------------
# Correlation Analysis
# -----------------------------------------

def to_bit(val):
    return 1 if val == 1 or val is True else 0

# Extracting values for correlation
sp_vals = [to_bit(r[0]) for r in results]
ndx_vals = [to_bit(r[1]) for r in results]
ftse_vals = [to_bit(r[2]) for r in results]
rate_vals = [to_bit(r[3]) for r in results]

print("\n--- Market Correlations (Calculated via NumPy) ---")
print(f"SP–NDX:   {np.corrcoef(sp_vals, ndx_vals)[0, 1]:.3f}")
print(f"SP–FTSE:  {np.corrcoef(sp_vals, ftse_vals)[0, 1]:.3f}")
print(f"RATE–NDX: {np.corrcoef(rate_vals, ndx_vals)[0, 1]:.3f}")
