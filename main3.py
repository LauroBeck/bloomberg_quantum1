import pandas as pd

def show_gate_map():
    data = [
        ["1", "Ry(2θ)", "Rotation on Y-axis for all 4 qubits.", "Intrinsic Volatility: Baseline Up/Down probability."],
        ["2", "CNOT(SP, NDX)", "SP500 is Control, Nasdaq is Target.", "Tech Correlation: NDX follows SP500 movement."],
        ["3", "CNOT(RATE, NDX)", "Rates is Control, Nasdaq is Target.", "Rate Sensitivity: Rates 'flip' Tech performance."],
        ["4", "CNOT(SP, FTSE)", "SP500 is Control, FTSE is Target.", "Global Spillover: FTSE reacts to US momentum."],
        ["5", "Measure", "Collapse the wave function.", "Market Close: Realizing the daily price action."]
    ]

    columns = ["Step", "Operation", "Description", "Financial Interpretation"]
    
    # Create DataFrame
    df_map = pd.DataFrame(data, columns=columns)

    print("\n" + "="*85)
    print(" QUANTUM MARKET ALGORITHM: GATE MAP")
    print("="*85)
    # Use to_string to ensure the whole table prints without truncation
    print(df_map.to_string(index=False))
    print("="*85 + "\n")

if __name__ == "__main__":
    show_gate_map()
