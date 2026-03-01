
import qsharp
from collections import Counter
import numpy as np

# Initialize Q# project
qsharp.init(project_root=".")

print("=== 4-Qubit Macro Market Simulation ===")

shots = 1000
results = []

for _ in range(shots):
    r = qsharp.eval(
        "BloombergQuantum.EncodeMarketState(0.4, 0.6, 0.3, 0.5)"
    )
    results.append(r)

counts = Counter(results)

print("\nState Distribution:")
for state, count in counts.items():
    print(f"{state} → {count}")

# -----------------------------------------
# Correlation Analysis
# -----------------------------------------

def bit(x):
    return 1 if x == qsharp.Result.One else 0

sp_vals = []
ndx_vals = []
ftse_vals = []
rate_vals = []

for state, count in counts.items():
    for _ in range(count):
        sp_vals.append(bit(state[0]))
        ndx_vals.append(bit(state[1]))
        ftse_vals.append(bit(state[2]))
        rate_vals.append(bit(state[3]))

print("\nCorrelations:")
print("SP–NDX:", round(np.corrcoef(sp_vals, ndx_vals)[0, 1], 3))
print("SP–FTSE:", round(np.corrcoef(sp_vals, ftse_vals)[0, 1], 3))
print("RATE–NDX:", round(np.corrcoef(rate_vals, ndx_vals)[0, 1], 3))
=======
# main.py
print("Welcome to Beck Quantum Python Project!")

