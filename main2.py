import qsharp
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

# Initialize
qsharp.init(project_root=".")

def run_market_sim(shots=1000):
    print(f"🚀 Running {shots} Market Scenarios...")
    results = []
    
    for _ in range(shots):
        # Parameters: (SP, NDX, FTSE, RATE)
        r = qsharp.eval("BloombergQuantum.EncodeMarketState(0.4, 0.6, 0.3, 0.5)")
        results.append([int(b) for b in r])

    # Convert to DataFrame
    df = pd.DataFrame(results, columns=['SP500', 'NASDAQ', 'FTSE', 'RATES'])
    
    # Calculate Correlation Matrix
    corr = df.corr()
    
    print("\n--- Correlation Matrix ---")
    print(corr)

    # 🎨 Visualizing the results
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title("Quantum Market Correlation Heatmap")
    plt.show()

if __name__ == "__main__":
    run_market_sim()
